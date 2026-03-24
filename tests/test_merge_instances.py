# tests/test_merge_instances.py
import ruamel.yaml
import rd_cdm.utils.merge_instances as merge_mod
from rd_cdm.utils.config import PathsConfig


def test_merge_instances_writes_rd_cdm_yaml(tmp_path, monkeypatch):
    """main() should merge the three part YAMLs into rd_cdm.yaml
    with rd_cdm_version and rd_cdm_date from the schema."""

    # flat instances dir (no version subdir)
    inst_dir = tmp_path / "src" / "rd_cdm" / "instances"
    inst_dir.mkdir(parents=True, exist_ok=True)

    schema_dir = tmp_path / "src" / "rd_cdm" / "schema"
    schema_dir.mkdir(parents=True, exist_ok=True)

    # minimal part YAMLs
    (inst_dir / "code_systems.yaml").write_text(
        "code_systems:\n  - {id: HP, version: v1}\n"
    )
    (inst_dir / "data_elements.yaml").write_text(
        "data_elements:\n  - {elementName: E, elementCode: {system: HP, code: '0000118'}}\n"
    )
    (inst_dir / "value_sets.yaml").write_text(
        "value_sets:\n  - {id: VS1, codes: ['HP:0000118']}\n"
    )

    # minimal schema with version and date
    (schema_dir / "rd_cdm.yaml").write_text(
        "id: https://example.org/rd-cdm\nversion: 2.0.3\ndate: '2025-03-24'\n"
    )

    # patch resolve_paths to return our tmp dirs
    src_root = tmp_path / "src"
    monkeypatch.setattr(
        merge_mod,
        "resolve_paths",
        lambda: PathsConfig(src_root=src_root, instances_dir=inst_dir),
    )

    rc = merge_mod.main()
    assert rc == 0

    out_file = inst_dir / "rd_cdm.yaml"
    assert out_file.exists()

    yaml = ruamel.yaml.YAML(typ="safe")
    merged = yaml.load(out_file.read_text())
    assert "code_systems" in merged
    assert "data_elements" in merged
    assert "value_sets" in merged
    assert merged["rd_cdm_version"] == "2.0.3"
    assert str(merged["rd_cdm_date"]) == "2025-03-24"