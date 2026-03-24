#!/usr/bin/env python3
from __future__ import annotations
import json
import argparse
import ruamel.yaml
from rd_cdm.utils.config import resolve_paths
import datetime

def _default(obj):
    if isinstance(obj, datetime.date):
        return str(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def main() -> int:
    """
    Convert the merged rd_cdm.yaml to rd_cdm.json.

    Reads from: src/rd_cdm/instances/rd_cdm.yaml
    Writes to:  src/rd_cdm/instances/jsons/rd_cdm.json

    The version (rd_cdm_version, rd_cdm_date) is already embedded in the
    merged YAML by the merge step and will appear at the top of the JSON.
    """
    paths = resolve_paths()
    merged_path = paths.instances_dir / "rd_cdm.yaml"
    if not merged_path.exists():
        print(f"ERROR: merged instance not found at {merged_path}. Run rd-cdm-merge first.")
        return 1

    out_dir = paths.instances_dir / "jsons"
    out_dir.mkdir(parents=True, exist_ok=True)

    yaml = ruamel.yaml.YAML()
    with merged_path.open("r", encoding="utf-8") as fh:
        data = yaml.load(fh) or {}

    out_path = out_dir / "rd_cdm.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=_default)

    version = data.get("rd_cdm_version", "unknown")
    print(f"✅ Wrote {out_path} (rd_cdm_version={version})")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Export merged RD-CDM YAML to JSON."
    )
    ap.parse_args()
    raise SystemExit(main())