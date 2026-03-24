#!/usr/bin/env python3
from __future__ import annotations
import csv
import sys
import argparse
import ruamel.yaml
from pathlib import Path
from rd_cdm.utils.config import resolve_paths


def _write_csv(rows: list[dict], out_path: Path) -> None:
    header_keys = sorted(
        {k for r in rows for k in (r.keys() if isinstance(r, dict) else [])}
    ) or ["id"]
    with out_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header_keys, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            flat = {
                k: (repr(v) if isinstance((v := r.get(k, "")), (list, dict)) else v)
                for k in header_keys
            }
            w.writerow(flat)


def main() -> int:
    """
    Export the merged rd_cdm.yaml to CSV files.

    Reads from: src/rd_cdm/instances/rd_cdm.yaml
    Writes to:  src/rd_cdm/instances/csvs/
      - code_systems.csv
      - data_elements.csv
      - value_sets.csv
      - rd_cdm.csv  (combined, with _section column and _metadata row for version)

    The version (rd_cdm_version, rd_cdm_date) appears as the first row in the
    combined rd_cdm.csv under section '_metadata'.
    """
    paths = resolve_paths()
    merged_path = paths.instances_dir / "rd_cdm.yaml"
    if not merged_path.exists():
        print(f"ERROR: merged instance not found at {merged_path}. Run rd-cdm-merge first.")
        return 1

    out_dir = paths.instances_dir / "csvs"
    out_dir.mkdir(parents=True, exist_ok=True)

    yaml = ruamel.yaml.YAML()
    with merged_path.open("r", encoding="utf-8") as fh:
        data = yaml.load(fh) or {}

    rd_cdm_version = data.get("rd_cdm_version", "unknown")
    rd_cdm_date = data.get("rd_cdm_date", "unknown")

    def _to_rows(raw) -> list[dict]:
        rows = []
        for row in (raw or []):
            if row is None:
                rows.append({})
            elif isinstance(row, dict):
                rows.append(row)
            else:
                rows.append({"value": row})
        return rows

    code_systems  = _to_rows(data.get("code_systems", []))
    data_elements = _to_rows(data.get("data_elements", []))
    value_sets    = _to_rows(data.get("value_sets", []))

    _write_csv(code_systems,  out_dir / "code_systems.csv")
    _write_csv(data_elements, out_dir / "data_elements.csv")
    _write_csv(value_sets,    out_dir / "value_sets.csv")

    # Combined CSV — version as first metadata row
    all_rows = (
        [("_metadata", {"rd_cdm_version": rd_cdm_version, "rd_cdm_date": str(rd_cdm_date)})] +
        [("code_systems",  r) for r in code_systems] +
        [("data_elements", r) for r in data_elements] +
        [("value_sets",    r) for r in value_sets]
    )
    key_union: set[str] = set()
    for _, r in all_rows:
        if isinstance(r, dict):
            key_union.update(r.keys())
    header = ["_section"] + sorted(key_union) if key_union else ["_section", "id"]

    combined_path = out_dir / "rd_cdm.csv"
    with combined_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        w.writeheader()
        for section, r in all_rows:
            row = {"_section": section}
            for k in header[1:]:
                v = r.get(k, "")
                row[k] = repr(v) if isinstance(v, (list, dict)) else v
            w.writerow(row)

    print(
        f"✅ Wrote CSVs to {out_dir}: "
        f"code_systems.csv, data_elements.csv, value_sets.csv, rd_cdm.csv "
        f"(rd_cdm_version={rd_cdm_version})"
    )
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Export merged RD-CDM YAML to CSV files."
    )
    ap.parse_args()
    raise SystemExit(main())