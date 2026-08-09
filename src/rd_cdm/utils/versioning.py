# src/rd_cdm/utils/versioning.py
from __future__ import annotations

from pathlib import Path
from typing import Optional

import ruamel.yaml

# The LinkML schema is the single source of truth for the model version.
# pyproject.toml mirrors it; tests/test_versioning_consistency.py asserts they agree.
SCHEMA_RELATIVE_PATH = ("rd_cdm", "schema", "rd_cdm.yaml")


def _src_root() -> Path:
    return Path(__file__).resolve().parents[2]


def schema_path() -> Path:
    return _src_root().joinpath(*SCHEMA_RELATIVE_PATH)


def get_model_version() -> Optional[str]:
    """Return the model version declared in the LinkML schema."""
    path = schema_path()
    if not path.exists():
        return None
    yaml = ruamel.yaml.YAML(typ="safe")
    with path.open("r", encoding="utf-8") as fh:
        schema = yaml.load(fh) or {}
    return schema.get("version")


def get_model_date() -> Optional[str]:
    """Return the model release date declared in the LinkML schema.

    Stored as `annotations.rd_cdm_date`, not a top-level `date:`, because `date`
    is not a slot on the LinkML SchemaDefinition - a top-level one makes
    `linkml validate` and `gen-doc` fail to load the schema at all.
    """
    path = schema_path()
    if not path.exists():
        return None
    yaml = ruamel.yaml.YAML(typ="safe")
    with path.open("r", encoding="utf-8") as fh:
        schema = yaml.load(fh) or {}
    date = (schema.get("annotations") or {}).get("rd_cdm_date")
    return str(date) if date is not None else None


def get_package_version() -> Optional[str]:
    """Return the installed distribution version, or None outside an install."""
    try:
        from importlib.metadata import version

        return version("rd-cdm")
    except Exception:
        return None


def resolve_instances_dir(version: Optional[str] = None) -> Path:
    base = _src_root() / "rd_cdm" / "instances"
    if not base.is_dir():
        raise FileNotFoundError(f"No instances directory found at {base}")
    return base
