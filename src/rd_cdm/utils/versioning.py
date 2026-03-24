# src/rd_cdm/util/versioning.py
from __future__ import annotations
import os
import re
from pathlib import Path
from typing import Optional

# tomllib in 3.11+, tomli fallback for 3.10
try:
    import tomllib  # type: ignore[attr-defined]
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore[no-redef]

def get_model_version() -> Optional[str]:
    root = Path(__file__).resolve().parents[2]
    return _read_project_version(root / "pyproject.toml")

def resolve_instances_dir(version: Optional[str] = None) -> Path:
    root = Path(__file__).resolve().parents[2]
    base = root / "rd_cdm" / "instances"
    if not base.is_dir():
        raise FileNotFoundError(f"No instances directory found at {base}")
    return base