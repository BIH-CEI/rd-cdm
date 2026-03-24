# tests/test_versioning.py
from pathlib import Path
import rd_cdm.utils.versioning as ver


def test_resolve_instances_dir_returns_instances_path(tmp_path, monkeypatch):
    """resolve_instances_dir should return src/rd_cdm/instances/ directly."""
    root = tmp_path / "src"
    inst = root / "rd_cdm" / "instances"
    inst.mkdir(parents=True, exist_ok=True)

    # Patch Path(__file__).resolve().parents[2] -> root
    import rd_cdm.utils.versioning as ver_mod
    monkeypatch.setattr(ver_mod, "__file__", str(root / "rd_cdm" / "utils" / "versioning.py"))

    resolved = ver.resolve_instances_dir()
    assert resolved == inst


def test_resolve_instances_dir_raises_when_missing(tmp_path, monkeypatch):
    """Should raise FileNotFoundError if instances dir does not exist."""
    import rd_cdm.utils.versioning as ver_mod
    monkeypatch.setattr(ver_mod, "__file__", str(tmp_path / "rd_cdm" / "utils" / "versioning.py"))

    import pytest
    with pytest.raises(FileNotFoundError):
        ver.resolve_instances_dir()