from __future__ import annotations
from pathlib import Path
from pydantic import BaseModel, ConfigDict, Field
from pydantic_settings import BaseSettings

from rd_cdm.utils.versioning import (
    resolve_instances_dir,
    normalize_dir_to_version,
    version_to_tag,
)

class VersioningConfig(BaseSettings):
    """Controls which RD-CDM version/tag is used when resolving instance paths."""
    model_config = ConfigDict(env_prefix="RDCDM_", extra="ignore")
    version: str | None = Field(
        default=None,
        description='e.g. "2.0.1", "v2.0.1", or "v2_0_1" (None=latest)',
    )

class PathsConfig(BaseModel):
    """Resolved paths for the current run. Usually computed, not provided directly."""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    src_root: Path
    instances_dir: Path
    version_tag: str   # e.g. "v2_0_1"
    version_norm: str  # e.g. "2.0.1"

class ExportConfig(BaseSettings):
    """Controls which exports are produced and where."""
    model_config = ConfigDict(env_prefix="RDCDM_", extra="ignore")
    write_json: bool = True
    write_csv: bool = True

def resolve_paths(cfg: VersioningConfig) -> PathsConfig:
    instances_dir = resolve_instances_dir(cfg.version)
    src_root = instances_dir.parents[2]
    v_norm = normalize_dir_to_version(instances_dir.name) or instances_dir.name
    v_tag = version_to_tag(v_norm)
    return PathsConfig(
        src_root=src_root,
        instances_dir=instances_dir,
        version_tag=v_tag,
        version_norm=v_norm,
    )
