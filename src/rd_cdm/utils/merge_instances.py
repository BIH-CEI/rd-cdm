#!/usr/bin/env python3
from __future__ import annotations

import sys
import argparse
import ruamel.yaml
from rd_cdm.utils.config import VersioningConfig, PathsConfig
from rd_cdm.utils.versioning import resolve_instances_dir, normalize_dir_to_version, version_to_tag

def _resolve_paths(vc: VersioningConfig) -> PathsConfig:
    base = resolve_instances_dir(vc.version)
    v_norm = normalize_dir_to_version(base.name) or base.name
    v_tag = version_to_tag(v_norm)
    src_root = base.parents[2]
    return PathsConfig(src_root=src_root, instances_dir=base, version_tag=v_tag, version_norm=v_norm)


def main(version: str | None = None) -> int:
    """
    Merge versioned instance YAML parts into a single `rd_cdm_vX_Y_Z.yaml`.

    Version resolution order:
      1) Explicit `--version` argument (accepts "2.0.1", "v2.0.1", or "v2_0_1")
      2) Environment variable RDCDM_VERSION
      3) Version from `pyproject.toml` ([tool.poetry].version or [project].version)
      4) Latest directory under `src/rd_cdm/instances/` (by semantic version)

    What this script does:
      • Resolves the correct `src/rd_cdm/instances/{vTAG}/` directory.
      • Loads `code_systems.yaml`, `data_elements.yaml`, and `value_sets.yaml`
        using ruamel.yaml (preserving quotes/comments where possible).
      • Merges them into a structured mapping:
            {
              "code_systems":  [...],
              "data_elements": [...],
              "value_sets":    [...]
            }
      • Writes the merged result to `rd_cdm_vX_Y_Z.yaml` in the same versioned folder.
    """
    try:
        paths = _resolve_paths(VersioningConfig(version=version))
    except Exception as e:
        print(f"ERROR: could not resolve instances directory: {e}", file=sys.stderr)
        return 2

    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True

    def load_file(name: str):
        p = paths.instances_dir / name
        if not p.exists():
            print(f"ERROR: missing required file: {p}", file=sys.stderr)
            sys.exit(1)
        with p.open("r", encoding="utf-8") as fh:
            return yaml.load(fh)

    cs = load_file("code_systems.yaml") or {}
    de = load_file("data_elements.yaml") or {}
    vs = load_file("value_sets.yaml") or {}

    merged = {
        "code_systems":  cs.get("code_systems", []),
        "data_elements": de.get("data_elements", []),
        "value_sets":    vs.get("value_sets", []),
    }

    out = paths.instances_dir / f"rd_cdm_{paths.version_tag}.yaml"
    try:
        with out.open("w", encoding="utf-8") as f:
            yaml.dump(merged, f)
    except Exception as e:
        print(f"ERROR: failed to write {out}: {e}", file=sys.stderr)
        return 3

    print(f"Wrote {out}")
    return 0

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Merge RD-CDM instance YAMLs into rd_cdm_vX_Y_Z.yaml for a specific version.")
    p.add_argument("-v","--version", help='Version like "2.0.1", "v2.0.1", or "v2_0_1".')
    args = p.parse_args()
    raise SystemExit(main(args.version))