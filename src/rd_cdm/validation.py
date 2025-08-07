#!/usr/bin/env python3
import os
import sys
import re
import urllib.parse

import requests
import ruamel.yaml
from linkml_runtime.loaders import yaml_loader
from rd_cdm.python_classes.rd_cdm import RdCdm

# ——— CONFIG ——————————————————————————————————————————————
VALIDATION_SYSTEMS = {"SNOMEDCT", "LOINC", "HP", "NCIT"}
BP_BASE = "https://data.bioontology.org"

# ——— HELPERS —————————————————————————————————————————————
def bp_headers():
    key = os.getenv("BIOPORTAL_API_KEY")
    if not key:
        print("ERROR: BIOPORTAL_API_KEY not set", file=sys.stderr)
        sys.exit(2)
    return {"Authorization": f"apikey token={key}"}

def clean_code(raw) -> str:
    s = str(raw)
    return re.sub(r'[^A-Za-z0-9\.-]', '', s)

def get_remote_version(sys_id: str) -> str:
    r = requests.get(f"{BP_BASE}/ontologies/{sys_id}", headers=bp_headers())
    r.raise_for_status()
    latest = r.json()["links"].get("latest_submission")
    r2 = requests.get(latest, headers=bp_headers()); r2.raise_for_status()
    j = r2.json()
    return j.get("version") or j.get("versionNumber") or j.get("submissionDate")

def get_remote_label(sys_id: str, code: str, iri: str) -> str | None:
    h = bp_headers()
    # try CURIE
    curie = f"{sys_id}:{code}"
    r = requests.get(f"{BP_BASE}/ontologies/{sys_id}/classes/{urllib.parse.quote(curie, safe='')}", headers=h)
    if r.status_code == 200:
        return r.json().get("prefLabel")
    if r.status_code != 404:
        r.raise_for_status()
    # try full IRI
    full = f"{iri.rstrip('/')}/{code}"
    r2 = requests.get(f"{BP_BASE}/ontologies/{sys_id}/classes/{urllib.parse.quote(full, safe='')}", headers=h)
    if r2.status_code == 200:
        return r2.json().get("prefLabel")
    if r2.status_code != 404:
        r2.raise_for_status()
    return None

# ——— MAIN —————————————————————————————————————————————————
def main():
    # 1) load model
    model: RdCdm = yaml_loader.load("src/rd_cdm/instances/v2_0_0/rd_cdm_full.yaml", RdCdm)
    cs_map = {cs.id: cs for cs in model.code_systems}

    errors = []
    warnings = []
    valid_codes = []
    invalid_codes = []
    skipped_codes = []

    de_checked = 0
    vs_checked = 0

    # 2) version drifts
    for sys_id in VALIDATION_SYSTEMS:
        cs = cs_map.get(sys_id)
        if not cs:
            errors.append(f"{sys_id}: missing CodeSystem entry")
            continue
        try:
            live_v = get_remote_version(sys_id)
        except Exception as e:
            errors.append(f"{sys_id}: version fetch failed ({e})")
            continue
        if live_v != cs.version:
            warnings.append(f"{sys_id}: version drift (model={cs.version}, live={live_v})")

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
    merged = yaml.load(open("src/rd_cdm/instances/v2_0_0/rd_cdm_full.yaml"))
    for vs in merged.get("value_sets", []):
        for c in vs.get("codes", []):
            sys_id = c.get("system")
            raw_code = c.get("code")
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
                errors.append(f"VS {vs['id']}: missing member {curie}")
                invalid_codes.append(curie)
            else:
                valid_codes.append(curie)
                label0 = c.get("label")
                if label0 and label_live != label0:
                    warnings.append(f"VS {vs['id']}: label drift – {curie}: model='{label0}', live='{label_live}'")

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
