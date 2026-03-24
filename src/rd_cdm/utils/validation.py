#!/usr/bin/env python3
from __future__ import annotations
import sys
import argparse
import requests
import ruamel.yaml
from tqdm import tqdm
from rd_cdm.utils.config import resolve_paths
from rd_cdm.utils.validation_utils import clean_code, get_remote_version, get_remote_label
from rd_cdm.utils.settings import ValidationSettings

VALIDATION_SYSTEMS = {"SNOMEDCT", "LOINC", "HP", "NCIT"}
SKIP_VERSION_CHECK = {"CustomCode", "GA4GH", "HL7FHIR", "HGVS", "ICD11", "ISO3166"}


def main():
    ap = argparse.ArgumentParser(
        description="Validate RD-CDM ontology codes against BioPortal."
    )
    ap.parse_args()

    settings = ValidationSettings()
    if not settings.bioportal_api_key:
        print("ERROR: BIOPORTAL_API_KEY not set", file=sys.stderr)
        sys.exit(2)

    paths = resolve_paths()
    full_path = paths.instances_dir / "rd_cdm.yaml"
    if not full_path.exists():
        print(
            f"ERROR: merged instance not found at {full_path}. "
            "Run rd-cdm-merge first.",
            file=sys.stderr,
        )
        sys.exit(1)

    yaml_s = ruamel.yaml.YAML(typ="safe")
    with open(full_path, "r", encoding="utf-8") as fh:
        merged = yaml_s.load(fh) or {}

    cs_map = {
        cs["id"]: type("CS", (), {
            "id": cs["id"],
            "version": cs.get("version", ""),
            "namespace_iri": cs.get("namespace_iri", ""),
        })()
        for cs in merged.get("code_systems", [])
        if isinstance(cs, dict) and "id" in cs
    }

    errors, warnings, valid_codes, invalid_codes, skipped_codes = [], [], [], [], []
    de_checked = vs_checked = 0

    # Version drift check
    code_systems = [
        cs for cs in merged.get("code_systems", [])
        if isinstance(cs, dict) and cs.get("id") not in SKIP_VERSION_CHECK
    ]
    with tqdm(code_systems, desc="Checking code system versions", unit="cs") as pbar:
        for cs_dict in pbar:
            cs_id = cs_dict.get("id", "")
            pbar.set_postfix(cs=cs_id)
            try:
                live_v = get_remote_version(cs_id)
            except Exception as e:
                warnings.append(f"{cs_id}: could not fetch live version ({e})")
                continue
            model_v = cs_dict.get("version", "")
            if live_v != model_v:
                warnings.append(
                    f"{cs_id}: version drift – model={model_v}, live={live_v}"
                )

    # DataElement code validation
    data_elements = [
        de for de in merged.get("data_elements", [])
        if isinstance(de, dict)
    ]
    with tqdm(data_elements, desc="Validating data elements", unit="de") as pbar:
        for de in pbar:
            element_code = de.get("elementCode", {}) or {}
            sys_id = element_code.get("system")
            raw_code = element_code.get("code")
            de_name = de.get("elementName", "")
            ordinal = de.get("ordinal", "")
            pbar.set_postfix(de=f"{ordinal} {de_name[:20]}")

            if sys_id not in VALIDATION_SYSTEMS:
                continue
            if "=" in str(raw_code):
                skipped_codes.append(f"{sys_id}:{raw_code}")
                continue
            code = clean_code(raw_code)
            de_checked += 1
            cs = cs_map.get(sys_id)
            if not cs:
                warnings.append(f"DE {ordinal}: unknown code system '{sys_id}'")
                continue
            try:
                label_live = get_remote_label(sys_id, code, cs.namespace_iri)
            except requests.HTTPError:
                label_live = None

            curie = f"{sys_id}:{raw_code}"
            if not label_live:
                errors.append(f"DE {ordinal} {de_name}: missing term {curie}")
                invalid_codes.append(curie)
            else:
                valid_codes.append(curie)
                label0 = element_code.get("label")
                if label0 and label_live != label0:
                    warnings.append(
                        f"DE {ordinal} {de_name}: label drift – "
                        f"{curie}: model='{label0}', live='{label_live}'"
                    )

    # ValueSet code validation
    value_sets = merged.get("value_sets", [])
    all_vs_codes = [
        (vs.get("id", "<unknown VS>"), c)
        for vs in value_sets
        for c in vs.get("codes", [])
    ]
    with tqdm(all_vs_codes, desc="Validating value set codes", unit="code") as pbar:
        for vs_id, c in pbar:
            if isinstance(c, dict):
                sys_id = c.get("system")
                raw_code = c.get("code")
                label0 = c.get("label")
            elif isinstance(c, str) and ":" in c:
                sys_id, raw_code = c.split(":", 1)
                label0 = None
            else:
                errors.append(f"VS {vs_id}: bad code entry {c!r}")
                continue

            pbar.set_postfix(vs=vs_id[:20], code=str(raw_code)[:15])

            if sys_id not in VALIDATION_SYSTEMS:
                continue
            if raw_code is None or "=" in str(raw_code):
                skipped_codes.append(f"{sys_id}:{raw_code}")
                continue

            code = clean_code(raw_code)
            vs_checked += 1
            cs = cs_map.get(sys_id)
            if not cs:
                warnings.append(f"VS {vs_id}: unknown code system '{sys_id}'")
                continue
            try:
                label_live = get_remote_label(sys_id, code, cs.namespace_iri)
            except requests.HTTPError:
                label_live = None

            curie = f"{sys_id}:{raw_code}"
            if not label_live:
                errors.append(f"VS {vs_id}: missing member {curie}")
                invalid_codes.append(curie)
            else:
                valid_codes.append(curie)
                if label0 and label_live != label0:
                    warnings.append(
                        f"VS {vs_id}: label drift – "
                        f"{curie}: model='{label0}', live='{label_live}'"
                    )

    # Summary
    rd_cdm_version = merged.get("rd_cdm_version", "unknown")
    print(f"\n=== RD-CDM VALIDATION SUMMARY (model version: {rd_cdm_version}) ===")
    print(f"  DataElements checked    : {de_checked}")
    print(f"  ValueSet members checked: {vs_checked}")
    print(f"  Valid terms             : {len(valid_codes)}")
    print(f"  Invalid (missing) terms : {len(invalid_codes)}")
    print(f"  Skipped terms           : {len(skipped_codes)}")
    print(f"  Warnings                : {len(warnings)}\n")

    if errors:
        print("Errors:")
        for e in errors:
            print(f"  • {e}")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  • {w}")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
