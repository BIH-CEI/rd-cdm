#!/usr/bin/env python3
from __future__ import annotations

import sys
import argparse
import ruamel.yaml

from rd_cdm.utils.versioning import resolve_instances_dir

def main(version: str | None = None) -> int:
    """
    Merge versioned instance YAML parts into a single `rd_cdm_full.yaml`.

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
      • Writes the merged result to `rd_cdm_full.yaml` in the same versioned folder.

    Parameters
    ----------
    version : str | None
        Optional version selector. If None, falls back to env/pyproject/latest.

    Returns
    -------
    int
        Exit code: 0 on success, non-zero if required files are missing or write fails.

    Notes
    -----
    • This script assumes the three source files exist in the resolved instances dir.
      If any are missing, it aborts with a clear error message.
    • ruamel.yaml is used (not PyYAML) to better preserve formatting semantics.
    """
    # 1) Resolve the versioned instances directory
    try:
        base = resolve_instances_dir(version)
    except Exception as e:
        print(f"ERROR: could not resolve instances directory: {e}", file=sys.stderr)
        return 2

    # 2) YAML loader setup
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True

    def load_file(name: str):
        """
        Load a YAML file named `name` from the resolved instances directory.

        This helper:
          • Builds the file path as `<instances_dir>/<name>`.
          • Verifies existence; on missing file, prints an error and exits.
          • Returns the parsed Python object produced by ruamel.yaml.

        Parameters
        ----------
        name : str
            Filename to load (e.g., "code_systems.yaml").

        Returns
        -------
        Any
            Parsed YAML content (typically a dict-like object).
        """
        p = base / name
        if not p.exists():
            print(f"ERROR: missing required file: {p}", file=sys.stderr)
            sys.exit(1)
        with p.open("r", encoding="utf-8") as fh:
            return yaml.load(fh)

    # 3) Load the three parts
    cs = load_file("code_systems.yaml")
    de = load_file("data_elements.yaml")
    vs = load_file("value_sets.yaml")

    # 4) Merge with safe .get() defaults
    merged = {
        "code_systems":  (cs or {}).get("code_systems", []),
        "data_elements": (de or {}).get("data_elements", []),
        "value_sets":    (vs or {}).get("value_sets", []),
    }

    # 5) Write out to the same versioned instances directory
    out = base / "rd_cdm_full.yaml"
    try:
        with out.open("w", encoding="utf-8") as f:
            yaml.dump(merged, f)
    except Exception as e:
        print(f"ERROR: failed to write {out}: {e}", file=sys.stderr)
        return 3

    print(f"Wrote {out}")
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Merge RD-CDM instance YAMLs into rd_cdm_full.yaml for a specific version."
    )
    parser.add_argument(
        "-v", "--version",
        help='Version like "2.0.1", "v2.0.1", or "v2_0_1". If omitted, uses env/pyproject/latest.'
    )
    args = parser.parse_args()
    raise SystemExit(main(args.version))
