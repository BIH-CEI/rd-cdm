from __future__ import annotations
from pathlib import Path
from pydantic import BaseModel, ConfigDict, Field
from pydantic_settings import BaseSettings

from rd_cdm.utils.versioning import (
    resolve_instances_dir
)

class PathsConfig(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    src_root: Path
    instances_dir: Path

class ExportConfig(BaseSettings):
    """Controls which exports are produced and where."""
    model_config = ConfigDict(env_prefix="RDCDM_", extra="ignore")
    write_json: bool = True
    write_csv: bool = True

def resolve_paths() -> PathsConfig:
    instances_dir = resolve_instances_dir()
    src_root = instances_dir.parents[1]  # src/rd_cdm/instances -> src/
    return PathsConfig(src_root=src_root, instances_dir=instances_dir)