#!/usr/bin/env python3
"""Project the RD-CDM instance data into a documentable LinkML schema.

``gen-doc`` documents a *schema*. The RD-CDM's data elements and value sets are
*instances* of the five-class container in ``schema/rd_cdm.yaml``, so gen-doc
cannot see them - it renders ``Coding`` and ``ValueSet`` as abstract shapes and
never mentions element 6.1.11 or the codes it permits.

This writes ``schema/rd_cdm_profile.yaml``, a generated LinkML schema in which:

* each **value set** becomes an ``enum``, each member a permissible value whose
  ``meaning:`` is its CURIE, with ``displayLabel`` on ``title`` and
  ``status: inactive`` on LinkML's native ``deprecated``;
* each **data element** becomes a ``slot`` named ``<ordinal> <elementName>``,
  with ``slot_uri`` set to its element code and its value set as ``range``;
* each **section** becomes a ``class``.

Stock ``gen-doc`` then produces a browsable reference for the whole model. This
is a projection in the same sense as ``rd-cdm-json`` and ``rd-cdm-csv``, and is
regenerated rather than edited:

    poetry run rd-cdm-profile
"""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from typing import Any

import ruamel.yaml

from rd_cdm.utils.config import resolve_paths
from rd_cdm.utils.versioning import get_model_date, get_model_version

#: Values of ``DataElement.valueSet`` that mean "no value set".
NO_VALUE_SET = {"", "n/a", "na", "none", "null", "-"}

#: Trailing version suffix on value set labels, e.g. "... Value Set v2.0.0".
VERSION_SUFFIX = re.compile(r"\s*v\d+(?:\.\d+)*\s*$")

#: A leading ordinal on a section label, e.g. "6.4 Family History".
SECTION_ORDINAL = re.compile(r"^\s*\d+(?:\.\d+)*\.?\s*")

#: Characters that break a generated filename or a Markdown link. gen-doc turns
#: spaces into underscores but passes everything else straight through, so a
#: slash becomes a path separator (6.4.2 "Propositus/-a") and brackets break the
#: link syntax (6.1.14 "Clinical Significance [ACMG]"). The untouched element
#: name is kept as the slot's title, which is what the page heading shows.
UNSAFE_IN_NAME = re.compile(r"[\\/\[\]<>:\"'|?*#]")

OUTPUT_NAME = "rd_cdm_profile.yaml"


def _pascal(text: str) -> str:
    parts = re.split(r"[^0-9A-Za-z]+", text or "")
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def _section_label(raw: str) -> str:
    """Strip the leading ordinal: '6.4 Family History' -> 'Family History'."""
    return SECTION_ORDINAL.sub("", raw or "").strip() or "Unsectioned"


def _slot_name(ordinal: str, element_name: str) -> str:
    """A filename- and link-safe slot name carrying the ordinal."""
    safe = UNSAFE_IN_NAME.sub("", element_name or "")
    safe = re.sub(r"\s+", " ", safe).strip()
    return f"{ordinal} {safe}".strip()


def _group_key(ordinal: str) -> str:
    """Group by ordinal prefix rather than by the section string.

    The section labels are not consistent - 6.4.0-6.4.5 say '6.4 Family
    History' while 6.4.6-6.4.13 say '6.4 Family' - so grouping on them would
    split one section into two classes. Ordinals are reliable.
    """
    parts = str(ordinal).split(".")
    return ".".join(parts[:2]) if len(parts) > 2 else parts[0]


def _is_curie_safe(code: Any) -> bool:
    """Whether a code can be used in a CURIE.

    Post-coordinated SNOMED expressions such as
    ``439272007:704321009=363778006`` are not CURIEs and break prefix
    expansion, so they are recorded as an annotation instead of a slot_uri.
    """
    text = str(code)
    return bool(text) and ":" not in text and "=" not in text


def _curie(coding: dict) -> str:
    return f"{coding.get('system')}:{coding.get('code')}"


def _annotations(**kwargs: Any) -> dict:
    return {k: str(v) for k, v in kwargs.items() if v not in (None, "", "n/a")}


def build_enums(value_sets: list[dict]) -> tuple[dict, dict]:
    """Return (enums, {value set label: enum name})."""
    enums: dict[str, dict] = {}
    by_label: dict[str, str] = {}

    for vs in value_sets:
        label = vs.get("label", "")
        name = _pascal(VERSION_SUFFIX.sub("", label))
        if name in enums:
            raise SystemExit(
                f"ERROR: two value sets project onto the enum '{name}'. "
                "Value set labels must be distinct - see structure_checks."
            )
        by_label[label] = name

        members = {_curie(c): c for c in vs.get("codes", []) if isinstance(c, dict)}
        permissible: dict[str, dict] = {}
        for curie, c in members.items():
            pv: dict[str, Any] = {"meaning": curie, "description": c.get("label")}
            if c.get("displayLabel"):
                pv["title"] = c["displayLabel"]
            if c.get("status") == "inactive":
                successor = c.get("replacedBy")
                if successor:
                    target = members.get(successor, {})
                    suffix = f" ({target['label']})" if target.get("label") else ""
                    # gen-doc resolves deprecated_element_has_exact_replacement as
                    # a *schema element* reference, so a code CURIE renders as
                    # NONE. The successor goes in the description, which shows.
                    pv["description"] = (
                        f"{c.get('label')} - INACTIVE, use {successor}{suffix}"
                    )
                pv["deprecated"] = " ".join((c.get("statusNote") or "").split())
            permissible[curie] = {k: v for k, v in pv.items() if v}

        enums[name] = {
            "description": f"Permitted codes for {label} (value set {vs.get('id')}).",
            "permissible_values": permissible,
        }

    return enums, by_label


def build_classes_and_slots(
    data_elements: list[dict], enum_for_label: dict[str, str]
) -> tuple[dict, dict]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for de in data_elements:
        groups[_group_key(de.get("ordinal", ""))].append(de)

    classes: dict[str, dict] = {}
    slots: dict[str, dict] = {}

    for key in sorted(groups, key=lambda k: [int(p) for p in k.split(".")]):
        members = groups[key]
        labels = Counter(_section_label(de.get("section", "")) for de in members)
        label = labels.most_common(1)[0][0]
        class_name = _pascal(label)

        slot_names = []
        for de in members:
            ordinal = str(de.get("ordinal", "")).strip()
            element_name = str(de.get("elementName", "")).strip()
            slot_name = _slot_name(ordinal, element_name)
            if slot_name in slots:
                raise SystemExit(
                    f"ERROR: two elements project onto the slot '{slot_name}'"
                )

            code = de.get("elementCode") or {}
            body: dict[str, Any] = {
                "title": f"{ordinal} {element_name}".strip(),
                "description": de.get("description"),
                "annotations": _annotations(
                    ordinal=ordinal,
                    section=de.get("section"),
                    element_code_label=code.get("label"),
                    data_type=de.get("dataType"),
                    data_specification=", ".join(de.get("dataSpecification") or []) or None,
                    fhir_expression=de.get("fhirExpression_v4_0_1"),
                    fhir_datatype=de.get("recommendedDataSpec_fhir"),
                    phenopacket_element=de.get("phenopacketSchemaElement_v2_0"),
                    phenopacket_datatype=de.get("recommendedDataSpec_phenopackets"),
                ),
            }
            if _is_curie_safe(code.get("code")):
                body["slot_uri"] = _curie(code)
            else:
                body["annotations"]["element_code"] = _curie(code)

            raw = de.get("valueSet")
            if raw is not None and str(raw).strip().lower() not in NO_VALUE_SET:
                vs_label = str(raw).strip()
                if vs_label not in enum_for_label:
                    raise SystemExit(
                        f"ERROR: {ordinal} references undeclared value set "
                        f"'{vs_label}' - run rd-cdm-validate --offline"
                    )
                body["range"] = enum_for_label[vs_label]

            slots[slot_name] = {k: v for k, v in body.items() if v}
            slot_names.append(slot_name)

        classes[class_name] = {
            "description": f"{key}. {label}",
            "slots": slot_names,
        }

    return classes, slots


def build(merged: dict, version: str, date: str) -> dict:
    prefixes = {
        cs["id"]: cs["namespace_iri"]
        for cs in merged.get("code_systems", [])
        if isinstance(cs, dict) and cs.get("id") and cs.get("namespace_iri")
    }
    prefixes.setdefault("rdcdm", "https://github.com/BIH-CEI/rd-cdm/")
    prefixes["linkml"] = "https://w3id.org/linkml/"

    enums, enum_for_label = build_enums(merged.get("value_sets", []) or [])
    classes, slots = build_classes_and_slots(
        merged.get("data_elements", []) or [], enum_for_label
    )

    return {
        "id": "https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml",
        "name": "rd-cdm-profile",
        "title": f"RD-CDM {version} - data elements and value sets",
        "description": (
            "The RD-CDM's data elements and value sets, projected from the "
            "instance data into LinkML so they can be browsed and referenced. "
            "GENERATED by rd-cdm-profile - do not edit by hand."
        ),
        "version": version,
        "annotations": {"rd_cdm_date": date},
        "license": "CC0",
        "prefixes": prefixes,
        "default_prefix": "rdcdm",
        "default_range": "string",
        "imports": ["linkml:types"],
        "classes": classes,
        "slots": slots,
        "enums": enums,
    }


def main() -> int:
    paths = resolve_paths()
    merged_path = paths.instances_dir / "rd_cdm.yaml"
    if not merged_path.exists():
        print(
            f"ERROR: merged instance not found at {merged_path}. Run rd-cdm-merge first.",
            file=sys.stderr,
        )
        return 2

    yaml = ruamel.yaml.YAML(typ="safe")
    with merged_path.open("r", encoding="utf-8") as fh:
        merged = yaml.load(fh) or {}

    profile = build(
        merged,
        version=get_model_version() or "unknown",
        date=get_model_date() or "unknown",
    )

    out = paths.src_root / "rd_cdm" / "schema" / OUTPUT_NAME
    writer = ruamel.yaml.YAML()
    writer.default_flow_style = False
    writer.width = 100
    with out.open("w", encoding="utf-8") as fh:
        fh.write(
            "# GENERATED by rd-cdm-profile from the instance data.\n"
            "# Do not edit by hand - run `poetry run rd-cdm-profile`.\n"
        )
        writer.dump(profile, fh)

    print(
        f"✅ Wrote {out} "
        f"({len(profile['classes'])} classes, {len(profile['slots'])} slots, "
        f"{len(profile['enums'])} enums)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
