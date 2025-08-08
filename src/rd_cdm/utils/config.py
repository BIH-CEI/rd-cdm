from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass(frozen=True)
class VersioningConfig:
    """
    Controls which RD-CDM version/tag is used when resolving instance paths.
    """
    version: Optional[str] = None  # "2.0.1", "v2.0.1", or "v2_0_1"

@dataclass(frozen=True)
class PathsConfig:
    """
    Resolved paths for the current run. Usually computed, not provided directly.
    """
    src_root: Path
    instances_dir: Path
    version_tag: str            # e.g. "v2_0_1"
    version_norm: str           # e.g. "2.0.1"

@dataclass(frozen=True)
class ExportConfig:
    """
    Controls which exports are produced and where.
    """
    write_json: bool = True
    write_csv: bool = True
