#!/usr/bin/env python3
import sys
import argparse
import requests
import ruamel.yaml
from linkml_runtime.loaders import yaml_loader
from rd_cdm.python_classes.rd_cdm import RdCdm
from rd_cdm.utils.versioning import resolve_instances_dir, normalize_dir_to_version, version_to_tag
from rd_cdm.utils.validation_utils import clean_code, get_remote_version, get_remote_label


# ——— CONFIG ——————————————————————————————————————————————
VALIDATION_SYSTEMS = {"SNOMEDCT", "LOINC", "HP", "NCIT"}
SKIP_VERSION_CHECK = {"CustomCode", "GA4GH", "HL7FHIR", "HGVS", "ICD11", "ISO3166"}
BP_BASE = "https://data.bioontology.org"

# ——— MAIN —————————————————————————————————————————————————
def main():
    """
    Entry point for RD-CDM validation against BioPortal.

    What it does
    ------------
    1) Resolves the instances directory (from --version, pyproject version, or latest).
    2) Loads the merged LinkML instance (rd_cdm_vX_Y_Z.yaml) as RdCdm.
    3) Builds a map of CodeSystems and checks live version drift for each ontology
       (except those explicitly skipped).
    4) Validates every DataElement.elementCode (system+code):
       - Skips composite codes (contain '=').
       - Uses get_remote_label to verify existence and optionally detect label drift.
    5) Validates every ValueSet member (only items under 'codes', not the ValueSet id):
       - Accepts both dict entries (with system/code/label) and strings 'PREFIX:ID'.
       - Skips composite codes.
       - Uses get_remote_label as above.
    6) Prints a summary: counts of DataElements checked, ValueSet members checked,
       valid/missing/skipped terms, and number of warnings.
    7) Prints detailed Errors and Warnings sections.
    8) Exits with status 1 if any errors were found; otherwise exits 0.

    Inputs & configuration
    ----------------------
    - BIOPORTAL_API_KEY must be set in the environment for API calls to succeed.
    - VALIDATION_SYSTEMS controls which ontologies are validated for code existence.
    - SKIP_VERSION_CHECK lists ontologies for which version drift is ignored.

    Side effects
    ------------
    - Prints to stdout/stderr.
    - Terminates the process via sys.exit with 0 (success) or 1 (errors).

    Returns
    -------
    None
        (Terminates the process.)
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", help="Instances version (e.g., 2.0.1 or v2_0_1). "
                                      "Defaults to pyproject version, then latest dir.")
    args = ap.parse_args()

    instances_dir = resolve_instances_dir(args.version)

    # Build filename rd_cdm_vX_Y_Z.yaml from the resolved directory name
    v_norm = normalize_dir_to_version(instances_dir.name)      # "2.0.1"
    v_tag  = version_to_tag(v_norm or instances_dir.name)      # "v2_0_1"
    full_path = instances_dir / f"rd_cdm_{v_tag}.yaml"         # rd_cdm_v2_0_1.yaml

    # Backward-compatibility fallback if someone still has rd_cdm_full.yaml
    if not full_path.exists():
        print(f"ERROR: merged instance not found: {full_path}", file=sys.stderr)
        sys.exit(1)

    model: RdCdm = yaml_loader.load(str(full_path), RdCdm)
    cs_map = {cs.id: cs for cs in model.code_systems}

    errors, warnings = [], []
    valid_codes, invalid_codes, skipped_codes = [], [], []
    de_checked = vs_checked = 0
    
    # 2) Version drift checks for *all* code systems except the skips
    for cs in model.code_systems:
        if cs.id in SKIP_VERSION_CHECK:
            # skip these on purpose
            continue
        try:
            live_v = get_remote_version(cs.id)
        except Exception as e:
            warnings.append(f"{cs.id}: could not fetch live version ({e})")
            continue
        if live_v != cs.version:
            warnings.append(f"{cs.id}: version drift – model={cs.version}, live={live_v}")

    # 3) DataElement codes
    for de in model.data_elements:
        sys_id = de.elementCode.system
        raw_code = de.elementCode.code
        if sys_id not in VALIDATION_SYSTEMS:
            continue
        if "=" in str(raw_code):
            skipped_codes.append(f"{sys_id}:{raw_code}")
            continue
        code = clean_code(raw_code)
        de_checked += 1
        cs = cs_map[sys_id]
        try:
            label_live = get_remote_label(sys_id, code, cs.namespace_iri)
        except requests.HTTPError:
            label_live = None

        curie = f"{sys_id}:{raw_code}"
        if not label_live:
            errors.append(f"DE {de.ordinal} {de.elementName}: missing term {curie}")
            invalid_codes.append(curie)
        else:
            valid_codes.append(curie)
            label0 = getattr(de.elementCode, "label", None)
            if label0 and label_live != label0:
                warnings.append(f"DE {de.ordinal} {de.elementName}: label drift – {curie}: model='{label0}', live='{label_live}'")

    # 4) ValueSet codes (raw YAML)
    yaml = ruamel.yaml.YAML(typ="safe")
    with open(full_path, "r", encoding="utf-8") as fh:  
        merged = yaml.load(fh)

    for vs in merged.get("value_sets", []):
        vs_id = vs.get("id", "<unknown VS>")
        for c in vs.get("codes", []):
            # normalize entry → (sys_id, raw_code, label0)
            if isinstance(c, dict):
                sys_id = c.get("system")
                raw_code = c.get("code")
                label0 = c.get("label")
            elif isinstance(c, str) and ":" in c:
                sys_id, raw_code = c.split(":", 1)
                label0 = None
            else:
                errors.append(f"VS {vs_id}: bad code entry {c}")
                continue

            if sys_id not in VALIDATION_SYSTEMS:
                continue
            if raw_code is None or "=" in str(raw_code):
                skipped_codes.append(f"{sys_id}:{raw_code}")
                continue

            code = clean_code(raw_code)
            vs_checked += 1
            cs = cs_map[sys_id]

            try:
                label_live = get_remote_label(sys_id, code, cs.namespace_iri)
            except requests.HTTPError:
                label_live = None

            curie = f"{sys_id}:{raw_code}"
            if not label_live:
                errors.append(f"VS {vs_id}: missing member {curie}")
                invalid_codes.append(curie)
            else:
                # record valid
                valid_codes.append(curie)
                # optional label drift warning
                if label0 and label_live != label0:
                    warnings.append(
                        f"VS {vs_id}: label drift – {curie}: "
                        f"model='{label0}', live='{label_live}'"
                    )
                    
    # ——— SUMMARY PRINTOUT ————————————————————————————————
    print("\n=== RD‐CDM VALIDATION SUMMARY ===")
    print(f"  DataElements checked: {de_checked}")
    print(f"  ValueSet members checked: {vs_checked}")
    print(f"  Valid terms: {len(valid_codes)}")
    print(f"  Invalid (missing) terms: {len(invalid_codes)}")
    print(f"  Skipped terms: {len(skipped_codes)}")
    print(f"  Warnings: {len(warnings)}\n")

    if errors:
        print("Errors:")
        for e in errors:
            print(f"  • {e}")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  • {w}")

    # exit 1 on errors only
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
