import types
import rd_cdm.utils.csv_parsing as cp

def test_csv_parsing_writes_all_and_combined(tmp_path, monkeypatch):
    version_tag = "v2_0_1"
    src_dir = tmp_path / "src"
    inst_dir = src_dir / "rd_cdm" / "instances" / version_tag
    out_dir = inst_dir / "csvs"
    inst_dir.mkdir(parents=True, exist_ok=True)

    # minimal source YAMLs
    (inst_dir / "code_systems.yaml").write_text("code_systems:\n  - {id: HP, version: v1}\n")
    (inst_dir / "data_elements.yaml").write_text("data_elements:\n  - {elementName: E, elementCode: {system: HP, code: '0000118'}}\n")
    (inst_dir / "value_sets.yaml").write_text("value_sets:\n  - {id: VS1, codes: ['HP:0000118']}\n")

    # point resolver to our temp folder
    monkeypatch.setattr(cp, "resolve_instances_dir", lambda ver=None: inst_dir)
    # avoid ruamel dependency variability: use safe loader behavior
    import ruamel.yaml
    yaml = ruamel.yaml.YAML(typ="safe")
    monkeypatch.setattr(cp, "ruamel", types.SimpleNamespace(yaml=types.SimpleNamespace(YAML=lambda: yaml)))

    rc = cp.write_csvs_from_instances(None)
    assert rc == 0

    # per-list CSVs
    assert (out_dir / "code_systems.csv").exists()
    assert (out_dir / "data_elements.csv").exists()
    assert (out_dir / "value_sets.csv").exists()

    # combined file follows v-tag style (e.g., rd_cdm_v2_0_1.csv)
    assert (out_dir / "rd_cdm_v2_0_1.csv").exists()