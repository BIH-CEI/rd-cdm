import ruamel.yaml

import rd_cdm.utils.merge_instances as merge_mod 

def test_merge_instances_writes_rd_cdm_v_tag_yaml(tmp_path, monkeypatch):
    # fake repo skeleton: src/rd_cdm/instances/v2_0_1 with the 3 parts
    version_tag = "v2_0_1"
    inst_dir = tmp_path / "src" / "rd_cdm" / "instances" / version_tag
    inst_dir.mkdir(parents=True, exist_ok=True)

    (inst_dir / "code_systems.yaml").write_text("code_systems:\n  - {id: HP, version: v1}\n")
    (inst_dir / "data_elements.yaml").write_text("data_elements:\n  - {elementName: E, elementCode: {system: HP, code: '0000118'}}\n")
    (inst_dir / "value_sets.yaml").write_text("value_sets:\n  - {id: VS1, codes: ['HP:0000118']}\n")

    # point resolve_instances_dir() to our temp instance dir
    monkeypatch.setattr(
        merge_mod, "resolve_instances_dir",
        lambda ver=None: inst_dir
    )

    # run main()
    rc = merge_mod.main(None)
    assert rc == 0

    out_file = inst_dir / f"rd_cdm_{version_tag}.yaml"
    assert out_file.exists()

    # sanity: merged keys present
    yaml = ruamel.yaml.YAML(typ="safe")
    merged = yaml.load(out_file.read_text())
    assert "code_systems" in merged and "data_elements" in merged and "value_sets" in merged
