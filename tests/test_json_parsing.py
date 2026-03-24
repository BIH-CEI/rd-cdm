# tests/test_json_parsing.py
import json
import ruamel.yaml
import rd_cdm.utils.json_parsing as jp
from rd_cdm.utils.config import PathsConfig


def test_json_parsing_reads_merged_and_writes_json(tmp_path, monkeypatch):
    """main() should read rd_cdm.yaml and write jsons/rd_cdm.json."""

    inst_dir = tmp_path / "src" / "rd_cdm" / "instances"
    inst_dir.mkdir(parents=True, exist_ok=True)

    # write a minimal merged rd_cdm.yaml (as merge step would produce)
    merged_data = {
        "rd_cdm_version": "2.0.3",
        "rd_cdm_date": "2025-03-24",
        "code_systems": [{"id": "HP", "version": "v1"}],
        "data_elements": [{"elementName": "E"}],
        "value_sets": [{"id": "VS1"}],
    }
    yaml = ruamel.yaml.YAML()
    with (inst_dir / "rd_cdm.yaml").open("w") as f:
        yaml.dump(merged_data, f)

    src_root = tmp_path / "src"
    monkeypatch.setattr(
        jp,
        "resolve_paths",
        lambda: PathsConfig(src_root=src_root, instances_dir=inst_dir),
    )

    rc = jp.main()
    assert rc == 0

    out_file = inst_dir / "jsons" / "rd_cdm.json"
    assert out_file.exists()

    data = json.loads(out_file.read_text())
    assert data["rd_cdm_version"] == "2.0.3"
    assert "code_systems" in data
    assert "data_elements" in data
    assert "value_sets" in data