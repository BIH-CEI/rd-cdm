#!/usr/bin/env python3
import csv
import sys
from pathlib import Path
import ruamel.yaml

from rd_cdm.utils.versioning import (
    resolve_instances_dir,
    version_to_tag,
    normalize_dir_to_version,
)

def write_csvs_from_instances(version: str | None = None) -> int:
    """
    Export versioned RD-CDM instance YAMLs to CSV.

    Outputs in: src/rd_cdm/instances/{vTAG}/csvs/
      - code_systems.csv
      - data_elements.csv
      - value_sets.csv
      - rd_cdm_{version}.csv  (stacked view with a `_section` column)
    """
    # 1) Resolve instances dir
    try:
        base = resolve_instances_dir(version)
    except Exception as e:
        print(f"ERROR: could not resolve instances directory: {e}", file=sys.stderr)
        return 2

    # 2) Compute tags & dirs
    v_norm = normalize_dir_to_version(base.name)          # e.g., "2.0.1"
    v_tag  = version_to_tag(v_norm or base.name)          # e.g., "v2_0_1"
    src_dir = base.parents[2]                             # points to 'src'
    out_dir = src_dir / "rd_cdm" / "instances" / v_tag / "csvs"
    out_dir.mkdir(parents=True, exist_ok=True)

    # 3) YAML loader
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True

    def _load_toplist(filename: str, top_key: str) -> list[dict]:
        p = base / filename
        if not p.exists():
            print(f"ERROR: missing required file: {p}", file=sys.stderr)
            sys.exit(1)
        with p.open("r", encoding="utf-8") as fh:
            data = yaml.load(fh) or {}
        lst = data.get(top_key, [])
        if lst is None:
            lst = []
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

    # 4) Load lists
    code_systems  = _load_toplist("code_systems.yaml",  "code_systems")
    data_elements = _load_toplist("data_elements.yaml", "data_elements")
    value_sets    = _load_toplist("value_sets.yaml",    "value_sets")

    # 5) Writer helper
    def _write_csv(rows: list[dict], out_path: Path) -> None:
        header_keys = sorted({k for r in rows for k in (r.keys() if isinstance(r, dict) else [])})
        if not header_keys:
            header_keys = ["id"]
        with out_path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=header_keys, extrasaction="ignore")
            w.writeheader()
            for r in rows:
                flat = {}
                for k in header_keys:
                    v = r.get(k, "")
                    flat[k] = repr(v) if isinstance(v, (list, dict)) else v
                w.writerow(flat)

    # 6) Write per-list CSVs
    _write_csv(code_systems,  out_dir / "code_systems.csv")
    _write_csv(data_elements, out_dir / "data_elements.csv")
    _write_csv(value_sets,    out_dir / "value_sets.csv")

    # 7) Write combined rd_cdm_{version}.csv
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
    combined_path = out_dir / f"rd_cdm_{v_tag}.csv"
    with combined_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        w.writeheader()
        for _, section, r in all_rows:
            row = {"_section": section}
            for k in header[1:]:
                v = r.get(k, "")
                row[k] = repr(v) if isinstance(v, (list, dict)) else v
            w.writerow(row)

    print(f"✅ Wrote CSVs to {out_dir}: code_systems.csv, data_elements.csv, value_sets.csv, rd_cdm_{v_tag}.csv")
    return 0

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Export RD-CDM instance YAML lists to CSV for a given version.")
    p.add_argument("-v", "--version", help='Version like "2.0.1", "v2.0.1", or "v2_0_1". If omitted, uses env/pyproject/latest.')
    args = p.parse_args()
    raise SystemExit(write_csvs_from_instances(args.version))
