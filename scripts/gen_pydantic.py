#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import shlex
import subprocess
import sys

from rd_cdm.utils.versioning import (
    resolve_instances_dir,
    normalize_dir_to_version,
    version_to_tag,
)

def _run(cmd: list[str]) -> int:
    print("Running:", " ".join(shlex.quote(c) for c in cmd), flush=True)
    return subprocess.run(cmd).returncode

def main(version: str | None = None) -> int:
    """
    Generate Pydantic models from schema/rd_cdm.yaml into:
      src/rd_cdm/pydantic_models/{vTAG}/

    Tries in order:
      1) linkml CLI with --output (newer versions)
      2) linkml CLI with --directory (older versions)
      3) Python API fallback (PydanticGenerator)
    """
    try:
        inst_dir = resolve_instances_dir(version)
    except Exception as e:
        print(f"ERROR: could not resolve instances directory: {e}", file=sys.stderr)
        return 2

    v_norm = normalize_dir_to_version(inst_dir.name) or inst_dir.name
    v_tag  = version_to_tag(v_norm)

    repo_root = Path(__file__).resolve().parents[1]
    schema = repo_root / "src" / "rd_cdm" / "schema" / "rd_cdm.yaml"
    out_dir = repo_root / "src" / "rd_cdm" / "pydantic_models" / v_tag
    out_dir.mkdir(parents=True, exist_ok=True)

    if not schema.exists():
        print(f"ERROR: schema not found at {schema}", file=sys.stderr)
        return 2

    # 1) Newer CLI: --output
    rc = _run([
        "gen-pydantic",
        str(schema),
        "--output", str(out_dir),
        "--module-name", f"rd_cdm.pydantic_models.{v_tag}",
    ])
    if rc == 0:
        print(f"✅ Pydantic models written to {out_dir}")
        return 0

    print("⚠️  gen-pydantic with --output failed, trying legacy --directory ...", file=sys.stderr)

    # 2) Older CLI: --directory
    rc2 = _run([
        "gen-pydantic",
        "--directory", str(out_dir),
        "--module-name", f"rd_cdm.pydantic_models.{v_tag}",
        str(schema),
    ])
    if rc2 == 0:
        print(f"✅ Pydantic models written to {out_dir}")
        return 0

    print("⚠️  CLI attempts failed, trying Python API fallback ...", file=sys.stderr)

    # 3) Python API fallback
    try:
        from linkml.generators.pydanticgen import PydanticGenerator
        gen = PydanticGenerator(str(schema))
        # Newer linkml prefers serialize(directory=..., module_name=...)
        gen.serialize(directory=str(out_dir), module_name=f"rd_cdm.pydantic_models.{v_tag}")
        print(f"✅ Pydantic models written to {out_dir} (Python API)")
        return 0
    except Exception as e:
        print("ERROR: gen-pydantic failed via CLI and Python API", file=sys.stderr)
        print(f"Details: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--version", help='Version like "2.0.1" or "v2_0_1" (only used for output folder naming).')
    args = ap.parse_args()
    raise SystemExit(main(args.version))
