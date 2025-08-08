#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
from rd_cdm.utils.versioning import resolve_instances_dir, normalize_dir_to_version, version_to_tag

def main(version: str | None = None) -> int:
    """
    Generate Pydantic models from schema/rd_cdm.yaml into:
      src/rd_cdm/pydantic_models/{vTAG}/
    """
    try:
        inst_dir = resolve_instances_dir(version)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr); return 2

    v_norm = normalize_dir_to_version(inst_dir.name) or inst_dir.name
    v_tag = version_to_tag(v_norm)

    repo_root = Path(__file__).resolve().parents[1]
    schema = repo_root / "src" / "rd_cdm" / "schema" / "rd_cdm.yaml"
    out_dir = repo_root / "src" / "rd_cdm" / "pydantic_models" / v_tag
    out_dir.mkdir(parents=True, exist_ok=True)

    # Prefer CLI to avoid API changes across linkml versions
    # Equivalent CLI: gen-pydantic --directory <out_dir> --module-name rd_cdm.pydantic_models.<v_tag> <schema>
    import subprocess
    import shlex
    cmd = f"gen-pydantic --directory {shlex.quote(str(out_dir))} --module-name rd_cdm.pydantic_models.{v_tag} {shlex.quote(str(schema))}"
    print(f"Running: {cmd}")
    r = subprocess.run(cmd, shell=True)
    if r.returncode != 0:
        print("ERROR: gen-pydantic failed", file=sys.stderr)
        return r.returncode

    print(f"✅ Pydantic models written to {out_dir}")
    return 0

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("-v","--version", help='Instances version like "2.0.1" or "v2_0_1" (used only for output folder naming).')
    args = ap.parse_args()
    raise SystemExit(main(args.version))
