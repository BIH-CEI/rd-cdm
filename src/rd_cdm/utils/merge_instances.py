#!/usr/bin/env python3
from __future__ import annotations

import sys
import argparse
import ruamel.yaml
from rd_cdm.utils.config import resolve_paths


def _read_schema_meta(schema_path) -> dict:
    """Read version and date from the LinkML schema (single source of truth)."""
    yaml = ruamel.yaml.YAML()
    with schema_path.open("r", encoding="utf-8") as fh:
        schema = yaml.load(fh) or {}
    return {
        "rd_cdm_version": schema.get("version", "unknown"),
        "rd_cdm_date": schema.get("date", "unknown"),
    }


def main() -> int:
    """
    Merge RD-CDM instance YAML parts into a single `rd_cdm.yaml`.

    What this script does:
      • Resolves `src/rd_cdm/instances/` (no versioned subdirs).
      • Reads `rd_cdm_version` and `rd_cdm_date` from `schema/rd_cdm.yaml`
        (the single source of truth for the data model version).
      • Loads `code_systems.yaml`, `data_elements.yaml`, and `value_sets.yaml`.
      • Merges everything into a single structured `rd_cdm.yaml`:
            {
              "rd_cdm_version": "2.0.3",
              "rd_cdm_date":    "2025-03-24",
              "code_systems":  [...],
              "data_elements": [...],
              "value_sets":    [...]
            }
      • Writes the result to `src/rd_cdm/instances/rd_cdm.yaml`.
    """
    try:
        paths = resolve_paths()
    except Exception as e:
        print(f"ERROR: could not resolve instances directory: {e}", file=sys.stderr)
        return 2

    schema_path = paths.src_root / "rd_cdm" / "schema" / "rd_cdm.yaml"
    if not schema_path.exists():
        print(f"ERROR: schema not found at {schema_path}", file=sys.stderr)
        return 2

    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True

    def load_file(name: str) -> dict:
        p = paths.instances_dir / name
        if not p.exists():
            print(f"ERROR: missing required file: {p}", file=sys.stderr)
            sys.exit(1)
        with p.open("r", encoding="utf-8") as fh:
            return yaml.load(fh) or {}

    meta = _read_schema_meta(schema_path)
    cs = load_file("code_systems.yaml")
    de = load_file("data_elements.yaml")
    vs = load_file("value_sets.yaml")

    merged = {
        **meta,
        "code_systems":  cs.get("code_systems", []),
        "data_elements": de.get("data_elements", []),
        "value_sets":    vs.get("value_sets", []),
    }

    out = paths.instances_dir / "rd_cdm.yaml"
    try:
        with out.open("w", encoding="utf-8") as f:
            yaml.dump(merged, f)
    except Exception as e:
        print(f"ERROR: failed to write {out}: {e}", file=sys.stderr)
        return 3

    print(
        f"✅ Wrote {out} "
        f"(rd_cdm_version={meta['rd_cdm_version']}, "
        f"rd_cdm_date={meta['rd_cdm_date']})"
    )
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Merge RD-CDM instance YAMLs into rd_cdm.yaml."
    )
    ap.parse_args()
    raise SystemExit(main())