#!/usr/bin/env python3
from __future__ import annotations
import csv
import argparse
import sys
import ruamel.yaml
from pathlib import Path
from rd_cdm.utils.config import VersioningConfig, PathsConfig
from rd_cdm.utils.versioning import resolve_instances_dir, normalize_dir_to_version, version_to_tag

def _resolve_paths(vc: VersioningConfig) -> PathsConfig:
    base = resolve_instances_dir(vc.version)
    v_norm = normalize_dir_to_version(base.name) or base.name
    v_tag = version_to_tag(v_norm)
    src_root = base.parents[2]
    return PathsConfig(src_root=src_root, instances_dir=base, version_tag=v_tag, version_norm=v_norm)

def write_csvs_from_instances(version: str | None = None) -> int:
    """
    Export versioned RD-CDM instance YAMLs to CSV.

    Outputs in: src/rd_cdm/instances/{vTAG}/csvs/
      - code_systems.csv
      - data_elements.csv
      - value_sets.csv
      - rd_cdm_{version}.csv  (stacked view with a `_section` column)
    """
    paths = _resolve_paths(VersioningConfig(version=version))
    out_dir = paths.src_root / "rd_cdm" / "instances" / paths.version_tag / "csvs"
    out_dir.mkdir(parents=True, exist_ok=True)

    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True

    def _load_toplist(filename: str, top_key: str) -> list[dict]:
        p = paths.instances_dir / filename
        if not p.exists():
            print(f"ERROR: missing required file: {p}", file=sys.stderr)
            sys.exit(1)
        with p.open("r", encoding="utf-8") as fh:
            data = yaml.load(fh) or {}
        lst = data.get(top_key, []) or []
        if not isinstance(lst, list):
            print(f"ERROR: `{top_key}` in {filename} is not a list", file=sys.stderr)
            sys.exit(1)
        norm: list[dict] = []
        for row in lst:
            if row is None:
                norm.append({})
            elif isinstance(row, dict):
                norm.append(row)
            else:
                norm.append({"value": row})
        return norm

    code_systems  = _load_toplist("code_systems.yaml",  "code_systems")
    data_elements = _load_toplist("data_elements.yaml", "data_elements")
    value_sets    = _load_toplist("value_sets.yaml",    "value_sets")

    def _write_csv(rows: list[dict], out_path: Path) -> None:
        header_keys = sorted({k for r in rows for k in (r.keys() if isinstance(r, dict) else [])}) or ["id"]
        with out_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=header_keys, extrasaction="ignore")
            w.writeheader()
            for r in rows:
                flat = {k: (repr(v) if isinstance((v := r.get(k, "")), (list, dict)) else v) for k in header_keys}
                w.writerow(flat)

    _write_csv(code_systems,  out_dir / "code_systems.csv")
    _write_csv(data_elements, out_dir / "data_elements.csv")
    _write_csv(value_sets,    out_dir / "value_sets.csv")

    # combined
    all_rows = (
        [("_section", "code_systems", r)  for r in code_systems] +
        [("_section", "data_elements", r) for r in data_elements] +
        [("_section", "value_sets", r)    for r in value_sets]
    )
    key_union = set()
    for _, _, r in all_rows:
        if isinstance(r, dict):
            key_union.update(r.keys())
    header = ["_section"] + sorted(key_union) if key_union else ["_section", "id"]
    combined_path = out_dir / f"rd_cdm_{paths.version_tag}.csv"
    with combined_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        w.writeheader()
        for _, section, r in all_rows:
            row = {"_section": section}
            for k in header[1:]:
                v = r.get(k, "")
                row[k] = repr(v) if isinstance(v, (list, dict)) else v
            w.writerow(row)

    print(f"✅ Wrote CSVs to {out_dir}: code_systems.csv, data_elements.csv, value_sets.csv, {combined_path.name}")
    return 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-v","--version", help='Version like "2.0.1" / "v2.0.1" / "v2_0_1".')
    args = ap.parse_args()
    raise SystemExit(write_csvs_from_instances(args.version))
