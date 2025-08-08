#!/usr/bin/env python3
from __future__ import annotations
import json
import argparse
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.dumpers import json_dumper
from rd_cdm.python_classes.rd_cdm import RdCdm
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
    Convert LinkML instance YAMLs in the resolved versioned instances dir to JSON,
    writing them under: src/rd_cdm/instances/{vTAG}/jsons/
    Also creates a combined `rd_cdm_vX_Y_Z.json`.

    Notes
    -----
    • Skips already-merged YAMLs (rd_cdm_full.yaml and rd_cdm_v*.yaml) during per-file conversion.
    • The combined file name matches the merged YAML naming (rd_cdm_vX_Y_Z.json).
    """
    paths = _resolve_paths(VersioningConfig(version=version))
    out_dir = paths.src_root / "rd_cdm" / "instances" / paths.version_tag / "jsons"
    out_dir.mkdir(parents=True, exist_ok=True)

    yamls = list(paths.instances_dir.glob("*.yaml")) + list(paths.instances_dir.glob("*.yml"))
    if not yamls:
        print(f"⚠️  No YAML files found in {paths.instances_dir}")
        return 0

    ok, fail = 0, 0
    combined_data: dict[str, dict] = {}
    for yf in sorted(yamls):
        stem = yf.stem
        if stem.startswith("rd_cdm_full") or stem.startswith("rd_cdm_v"):
            continue
        try:
            obj = yaml_loader.load(str(yf), target_class=RdCdm)
            out_path = out_dir / (stem + ".json")
            json_str = json_dumper.dumps(obj)
            json_obj = json.loads(json_str)
            with out_path.open("w", encoding="utf-8") as f:
                json.dump(json_obj, f, indent=2, ensure_ascii=False)
            combined_data[stem] = json_obj
            print(f"✅ {yf.name} -> rd_cdm/instances/{paths.version_tag}/jsons/{out_path.name}")
            ok += 1
        except Exception as e:
            print(f"❌ {yf.name}: {e}")
            fail += 1

    combined_path = out_dir / f"rd_cdm_{paths.version_tag}.json"
    with combined_path.open("w", encoding="utf-8") as f:
        json.dump(combined_data, f, indent=2, ensure_ascii=False)

    print(f"\nDone. Wrote {ok} JSON(s); {fail} file(s) failed. Combined JSON at {combined_path}")
    return 0 if fail == 0 else 1

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-v","--version", help='Version like "2.0.1" / "v2.0.1" / "v2_0_1".')
    args = ap.parse_args()
    raise SystemExit(main(args.version))
