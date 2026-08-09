"""The LinkML schema is the single source of truth for the model version.

pyproject.toml has to carry its own copy for packaging, so this test asserts
the two agree - the failure mode being a release where the shipped model
reports a different version than the distribution.
"""
from __future__ import annotations
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # py3.10
    import tomli as tomllib

from rd_cdm.utils.versioning import get_model_version, schema_path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _pyproject_version() -> str:
    with (REPO_ROOT / "pyproject.toml").open("rb") as fh:
        return tomllib.load(fh)["tool"]["poetry"]["version"]


def test_schema_version_is_readable():
    assert schema_path().exists()
    assert get_model_version()


def test_pyproject_matches_schema():
    assert _pyproject_version() == get_model_version(), (
        "pyproject.toml version and schema/rd_cdm.yaml version disagree - "
        "the schema is the source of truth; update pyproject.toml to match."
    )


def test_merged_instance_matches_schema():
    import ruamel.yaml

    merged = REPO_ROOT / "src" / "rd_cdm" / "instances" / "rd_cdm.yaml"
    if not merged.exists():
        return
    yaml = ruamel.yaml.YAML(typ="safe")
    with merged.open("r", encoding="utf-8") as fh:
        doc = yaml.load(fh) or {}
    assert doc.get("rd_cdm_version") == get_model_version(), (
        "instances/rd_cdm.yaml is stale - run rd-cdm-merge"
    )
