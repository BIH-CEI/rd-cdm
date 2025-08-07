from pathlib import Path
import rd_cdm.utils.versioning as ver

def test_version_to_tag_and_normalize():
    assert ver.version_to_tag("2.0.1") == "v2_0_1"
    assert ver.version_to_tag("v2.0.1") == "v2_0_1"
    assert ver.normalize_dir_to_version("v2_0_1") == "2.0.1"
    assert ver.normalize_dir_to_version("garbage") is None


def test_resolve_instances_dir_with_env_and_existing_dir(tmp_path, monkeypatch):
    # Build temp structure that matches expected: <root>/rd_cdm/instances/v2_0_1
    root = tmp_path / "src"
    inst = root / "rd_cdm" / "instances" / "v2_0_1"
    inst.mkdir(parents=True, exist_ok=True)

    # Monkeypatch Path(__file__).resolve().parents[2] -> root
    class FakePath(Path):
        _flavour = Path(".")._flavour  # required for subclassing Path
        def resolve(self): return self
        @property
        def parents(self):
            # return something whose [2] is our `root`
            class _Parents(list):
                pass
            p = _Parents([self.parent, self.parent.parent, root])
            return p

    monkeypatch.setattr(ver, "Path", FakePath)

    # Set env so it uses 2.0.1
    monkeypatch.setenv("RDCDM_VERSION", "2.0.1")
    resolved = ver.resolve_instances_dir(None)
    # Using our FakePath, resolved should be a FakePath pointing at inst
    assert str(resolved).endswith("rd_cdm/instances/v2_0_1")
