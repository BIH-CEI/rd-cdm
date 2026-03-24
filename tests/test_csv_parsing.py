# tests/test_csv_parsing.py
import csv
import ruamel.yaml
import rd_cdm.utils.csv_parsing as cp
from rd_cdm.utils.config import PathsConfig


def test_csv_parsing_writes_all_and_combined(tmp_path, monkeypatch):
    """main() should write per-section CSVs and a combined rd_cdm.csv
    with a _metadata row carrying rd_cdm_version."""

    inst_dir = tmp_path / "src" / "rd_cdm" / "instances"
    inst_dir.mkdir(parents=True, exist_ok=True)

    # write a minimal merged rd_cdm.yaml
    merged_data = {
        "rd_cdm_version": "2.0.3",
        "rd_cdm_date": "2025-03-24",
        "code_systems": [{"id": "HP", "version": "v1"}],
        "data_elements": [{"elementName": "E", "elementCode": {"system": "HP", "code": "0000118"}}],
        "value_sets": [{"id": "VS1", "codes": ["HP:0000118"]}],
    }
    yaml = ruamel.yaml.YAML()
    with (inst_dir / "rd_cdm.yaml").open("w") as f:
        yaml.dump(merged_data, f)

    src_root = tmp_path / "src"
    monkeypatch.setattr(
        cp,
        "resolve_paths",
        lambda: PathsConfig(src_root=src_root, instances_dir=inst_dir),
    )

    rc = cp.main()
    assert rc == 0

    csv_dir = inst_dir / "csvs"
    assert (csv_dir / "code_systems.csv").exists()
    assert (csv_dir / "data_elements.csv").exists()
    assert (csv_dir / "value_sets.csv").exists()
    assert (csv_dir / "rd_cdm.csv").exists()

    # check _metadata row carries the version
    with (csv_dir / "rd_cdm.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    metadata_rows = [r for r in rows if r.get("_section") == "_metadata"]
    assert len(metadata_rows) == 1
    assert metadata_rows[0]["rd_cdm_version"] == "2.0.3"