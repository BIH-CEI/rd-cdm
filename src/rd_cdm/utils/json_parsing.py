#!/usr/bin/env python3
import json
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.dumpers import json_dumper

from rd_cdm.python_classes.rd_cdm import RdCdm
from rd_cdm.utils.versioning import (
    resolve_instances_dir,
    normalize_dir_to_version,
    version_to_tag,
)

def main(version: str | None = None) -> int:
    """
    Convert all LinkML instance YAMLs in the resolved versioned instances dir
    to JSON, writing them under src/rd_cdm/jsons/{vTAG}/.
    """
    # 1) Find the instances directory for the desired version
    instances_dir = resolve_instances_dir(version)
    v_norm = normalize_dir_to_version(instances_dir.name)  # e.g., "2.0.1"
    v_tag = version_to_tag(v_norm or instances_dir.name)   # e.g., "v2_0_1"

    # 2) Compute output directory alongside src/rd_cdm/
    # repo root: .../src/rd_cdm/instances/{v_tag} -> go up two to src/
    src_dir = instances_dir.parents[2]
    out_dir = src_dir / "rd_cdm" / "jsons" / v_tag
    out_dir.mkdir(parents=True, exist_ok=True)

    # 3) Find YAML files and convert
    yamls = list(instances_dir.glob("*.yaml")) + list(instances_dir.glob("*.yml"))
    if not yamls:
        print(f"⚠️  No YAML files found in {instances_dir}")
        return 0

    ok, fail = 0, 0
    for yf in sorted(yamls):
        try:
            obj = yaml_loader.load(str(yf), target_class=RdCdm)
            out_path = out_dir / (yf.stem + ".json")

            # Dump via json_dumper to a string, then pretty-print
            json_str = json_dumper.dumps(obj)  # no indent here
            json_obj = json.loads(json_str)    # parse back to dict
            with out_path.open("w", encoding="utf-8") as f:
                json.dump(json_obj, f, indent=2, ensure_ascii=False)

            print(f"✅ {yf.name} -> {out_path.relative_to(src_dir)}")
            ok += 1
        except Exception as e:
            print(f"❌ {yf.name}: {e}")
            fail += 1

    print(f"\nDone. Wrote {ok} JSON(s); {fail} file(s) failed.")
    return 0 if fail == 0 else 1

if __name__ == "__main__":
    # Optional: allow overriding via env RDCDM_VERSION or pyproject,
    # or pass an explicit version string like "2.0.1" or "v2_0_1".
    import argparse
    p = argparse.ArgumentParser(description="Convert LinkML instance YAMLs to JSON by version.")
    p.add_argument("--version", "-v", help='Version like "2.0.1" or "v2_0_1". If omitted, uses env/pyproject/latest.')
    args = p.parse_args()
    raise SystemExit(main(args.version))
