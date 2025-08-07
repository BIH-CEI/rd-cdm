import json
from pathlib import Path
import types

import rd_cdm.utils.json_parsing as jp


def test_json_parsing_skips_merged_and_writes_combined(tmp_path, monkeypatch):
    version_tag = "v2_0_1"
    src_dir = tmp_path / "src"
    inst_dir = src_dir / "rd_cdm" / "instances" / version_tag
    json_dir = inst_dir / "jsons"
    inst_dir.mkdir(parents=True, exist_ok=True)

    # create part YAMLs + a merged YAML that must be skipped in the loop
    (inst_dir / "code_systems.yaml").write_text("dummy")
    (inst_dir / "data_elements.yaml").write_text("dummy")
    (inst_dir / "value_sets.yaml").write_text("dummy")
    (inst_dir / "rd_cdm_v2_0_1.yaml").write_text("dummy")  # must be skipped

    # monkeypatch instance resolver
    monkeypatch.setattr(jp, "resolve_instances_dir", lambda ver=None: inst_dir)

    # monkeypatch loader + dumper to avoid LinkML dependency
    monkeypatch.setattr(jp, "yaml_loader", types.SimpleNamespace(
        load=lambda path, target_class: {"loaded_from": Path(path).name}
    ))
    monkeypatch.setattr(jp, "json_dumper", types.SimpleNamespace(
        dumps=lambda obj: json.dumps(obj)
    ))

    rc = jp.main(None)
    assert rc == 0

    # per-file JSONs (no rd_cdm_v*.json from the loop itself)
    assert (json_dir / "code_systems.json").exists()
    assert (json_dir / "data_elements.json").exists()
    assert (json_dir / "value_sets.json").exists()
    assert (json_dir / "rd_cdm_v2_0_1.json").exists()

    # combined file present with v-tag in name
    combined = json_dir / "rd_cdm_v2_0_1.json"
    assert combined.exists()
    data = json.loads(combined.read_text())
    assert set(data.keys()) == {"code_systems", "data_elements", "value_sets"}