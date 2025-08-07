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
    Convert LinkML instance YAMLs in the resolved versioned instances dir to JSON,
    writing them under: src/rd_cdm/instances/{vTAG}/jsons/
    Also creates a combined `rd_cdm_vX_Y_Z.json`.

    Notes
    -----
    • Skips already-merged YAMLs (rd_cdm_full.yaml and rd_cdm_v*.yaml) during per-file conversion.
    • The combined file name matches the merged YAML naming (rd_cdm_vX_Y_Z.json).
    """
    # 1) Find the instances directory for the desired version
    instances_dir = resolve_instances_dir(version)
    v_norm = normalize_dir_to_version(instances_dir.name)            # e.g., "2.0.1"
    v_tag  = version_to_tag(v_norm or instances_dir.name)            # e.g., "v2_0_1"

    # 2) Compute output directory inside instances dir
    src_dir = instances_dir.parents[2]
    out_dir = src_dir / "rd_cdm" / "instances" / v_tag / "jsons"
    out_dir.mkdir(parents=True, exist_ok=True)

    # 3) Find YAML files and convert (skip merged YAMLs)
    yamls = list(instances_dir.glob("*.yaml")) + list(instances_dir.glob("*.yml"))
    if not yamls:
        print(f"⚠️  No YAML files found in {instances_dir}")
        return 0

    ok, fail = 0, 0
    combined_data = {}
    for yf in sorted(yamls):
        stem = yf.stem
        # Skip merged YAMLs so we don't also emit rd_cdm_full.json / rd_cdm_v*.json from the loop
        if stem.startswith("rd_cdm_full") or stem.startswith("rd_cdm_v"):
            continue
        try:
            obj = yaml_loader.load(str(yf), target_class=RdCdm)
            out_path = out_dir / (stem + ".json")

            # Dump via linkml json_dumper, then pretty-print
            json_str = json_dumper.dumps(obj)
            json_obj = json.loads(json_str)
            with out_path.open("w", encoding="utf-8") as f:
                json.dump(json_obj, f, indent=2, ensure_ascii=False)

            # Add to combined dict
            combined_data[stem] = json_obj

            print(f"✅ {yf.name} -> {out_path.relative_to(src_dir)}")
            ok += 1
        except Exception as e:
            print(f"❌ {yf.name}: {e}")
            fail += 1

    # 4) Write combined rd_cdm_vX_Y_Z.json
    combined_path = out_dir / f"rd_cdm_{v_tag}.json"     # e.g., rd_cdm_v2_0_1.json
    with combined_path.open("w", encoding="utf-8") as f:
        json.dump(combined_data, f, indent=2, ensure_ascii=False)

    print(f"\nDone. Wrote {ok} JSON(s); {fail} file(s) failed. Combined JSON at {combined_path}")
    return 0 if fail == 0 else 1

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="Convert LinkML instance YAMLs to JSON by version.")
    p.add_argument("--version", "-v", help='Version like "2.0.1", "v2_0_1", or "v2.0.1". If omitted, uses env/pyproject/latest.')
    args = p.parse_args()
    raise SystemExit(main(args.version))
