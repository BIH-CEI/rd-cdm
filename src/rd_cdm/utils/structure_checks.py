"""Offline consistency checks over the merged RD-CDM instance.

These run without network access and without a BioPortal key, and cover the
class of defect BioPortal validation structurally cannot see: a value set that
is declared twice, a data element pointing at a value set that does not exist,
or a value set whose ``id`` no longer matches the data element it constrains.

The invariant the checks enforce is that **a value set's ``id`` is the CURIE of
the data element it constrains**. Data elements reference their value set by
*label*, so nothing else resolves the ``id`` and a stale one is otherwise
invisible - which is how ``SNOMEDCT:281053000`` survived the move of *Sex at
Birth* onto ``LOINC:76689-9``.

Used by ``rd-cdm-validate`` before it touches the network, and by
``tests/test_structure_checks.py`` in CI, where there is no key.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any, Iterable

#: Placeholders used in ``DataElement.valueSet`` to mean "no value set".
NO_VALUE_SET = {"", "n/a", "na", "none", "null", "-"}


def _is_value_set_reference(raw: Any) -> bool:
    if raw is None:
        return False
    return str(raw).strip().lower() not in NO_VALUE_SET


def _element_curie(de: dict) -> str | None:
    code = de.get("elementCode") or {}
    system, value = code.get("system"), code.get("code")
    if not system or value is None:
        return None
    return f"{system}:{value}"


def _de_name(de: dict) -> str:
    return f"DE {de.get('ordinal', '?')} {de.get('elementName', '')}".strip()


def check_structure(merged: dict) -> list[str]:
    """Return a list of structural problems in a merged RD-CDM document.

    An empty list means the value sets, data elements and their cross-references
    are internally consistent. Nothing here contacts BioPortal.
    """
    problems: list[str] = []

    value_sets = [vs for vs in merged.get("value_sets", []) or [] if isinstance(vs, dict)]
    data_elements = [de for de in merged.get("data_elements", []) or [] if isinstance(de, dict)]
    code_system_ids = {
        cs.get("id")
        for cs in merged.get("code_systems", []) or []
        if isinstance(cs, dict)
    }

    # -- value sets are declared once, under a unique id and a unique label ----
    for vs_id, count in Counter(vs.get("id") for vs in value_sets).items():
        if count > 1:
            problems.append(
                f"value set id '{vs_id}' is declared {count} times - "
                "every member is validated once per declaration"
            )
    for label, count in Counter(vs.get("label") for vs in value_sets).items():
        if count > 1:
            problems.append(
                f"value set label '{label}' is used by {count} value sets - "
                "data elements reference value sets by label, so this is ambiguous"
            )

    # -- members are declared once per value set, under a known code system ----
    for vs in value_sets:
        vs_id = vs.get("id", "<unknown>")
        codes = vs.get("codes", []) or []
        curies = [
            f"{c.get('system')}:{c.get('code')}"
            for c in codes
            if isinstance(c, dict)
        ]
        for curie, count in Counter(curies).items():
            if count > 1:
                problems.append(f"VS {vs_id}: member {curie} is listed {count} times")
        for c in codes:
            if not isinstance(c, dict):
                problems.append(f"VS {vs_id}: member is not a mapping: {c!r}")
                continue
            if code_system_ids and c.get("system") not in code_system_ids:
                problems.append(
                    f"VS {vs_id}: member {c.get('system')}:{c.get('code')} uses "
                    "a code system that is not declared in code_systems.yaml"
                )
            if c.get("status") == "inactive" and not c.get("statusNote"):
                problems.append(
                    f"VS {vs_id}: inactive member {c.get('system')}:{c.get('code')} "
                    "has no statusNote explaining the inactivation"
                )
            replaced_by = c.get("replacedBy")
            if replaced_by and c.get("status") != "inactive":
                problems.append(
                    f"VS {vs_id}: {c.get('system')}:{c.get('code')} declares "
                    "replacedBy but is not marked inactive"
                )
            if replaced_by and replaced_by not in curies:
                problems.append(
                    f"VS {vs_id}: {c.get('system')}:{c.get('code')} is replaced by "
                    f"{replaced_by}, which is not a member of this value set - a "
                    "legacy value could not be migrated without leaving it"
                )

        if codes and not any(
            c.get("status") in (None, "active")
            for c in codes
            if isinstance(c, dict)
        ):
            problems.append(
                f"VS {vs_id}: every member is inactive, so nothing can be captured"
            )

    # -- every referenced value set exists, and every value set is referenced ---
    by_label: dict[str, dict] = {}
    for vs in value_sets:
        by_label.setdefault(vs.get("label"), vs)

    referenced_by: dict[str, list[dict]] = defaultdict(list)
    for de in data_elements:
        raw = de.get("valueSet")
        if not _is_value_set_reference(raw):
            continue
        label = str(raw).strip()
        if label not in by_label:
            problems.append(
                f"{_de_name(de)}: references value set '{label}', which is not declared"
            )
            continue
        referenced_by[label].append(de)

    for vs in value_sets:
        label = vs.get("label")
        if label not in referenced_by:
            problems.append(
                f"VS {vs.get('id')} ('{label}') is declared but no data element uses it"
            )
            continue

        # -- the id is the CURIE of the element the value set constrains -------
        expected = {_element_curie(de) for de in referenced_by[label]} - {None}
        if expected and vs.get("id") not in expected:
            owners = ", ".join(sorted(_de_name(de) for de in referenced_by[label]))
            problems.append(
                f"VS {vs.get('id')} ('{label}'): id does not match the element code "
                f"of {owners} ({' or '.join(sorted(expected))})"
            )

    # -- sections are spelled consistently within an ordinal group ------------
    problems.extend(check_sections(merged))

    return problems


def check_sections(merged: dict) -> list[str]:
    """Every element sharing an ordinal prefix must carry the same section label.

    ``rd-cdm-profile`` turns each section into a class, so a section spelled two
    ways splits into two classes - which is what ``6.4 Family History`` and
    ``6.4 Family`` did. Grouping is by ordinal, so the inconsistency is silent
    unless it is checked for.
    """
    problems: list[str] = []
    groups: dict[str, set[str]] = defaultdict(set)

    for de in merged.get("data_elements", []) or []:
        if not isinstance(de, dict):
            continue
        parts = str(de.get("ordinal", "")).split(".")
        key = ".".join(parts[:2]) if len(parts) > 2 else parts[0]
        groups[key].add(str(de.get("section", "")).strip())

    for key, labels in sorted(groups.items()):
        if len(labels) > 1:
            spellings = ", ".join(f"'{label}'" for label in sorted(labels))
            problems.append(
                f"section {key} is spelled {len(labels)} ways ({spellings}) - "
                "one section must have one label"
            )

    return problems


def format_problems(problems: Iterable[str]) -> str:
    return "\n".join(f"  • {p}" for p in problems)
