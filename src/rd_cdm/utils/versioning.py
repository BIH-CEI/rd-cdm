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

def _read_project_version(pyproject_path: Path) -> Optional[str]:
    if not pyproject_path.exists():
        return None
    with pyproject_path.open("rb") as f:
        data = tomllib.load(f)

    # Poetry-style
    v = (
        data.get("tool", {})
            .get("poetry", {})
            .get("version")
    )
    # PEP 621 fallback ([project].version)
    if not v:
        v = data.get("project", {}).get("version")
    return str(v) if v else None

def version_to_tag(version: str) -> str:
    """
    Map "2.0.1" or "v2.0.1" or "v2_0_1" -> "v2_0_1".
    """
    v = version.strip()
    v = re.sub(r"^[vV]", "", v)
    v = v.replace(".", "_")
    return f"v{v}"

def normalize_dir_to_version(name: str) -> Optional[str]:
    """
    Map "v2_0_1" -> "2.0.1" (used for sorting dirs).
    """
    n = re.sub(r"^[vV]", "", name)
    n = n.replace("_", ".")
    if re.fullmatch(r"\d+(\.\d+){1,}", n):
        return n
    return None

def resolve_instances_dir(version: Optional[str] = None) -> Path:
    """
    Determine the instances directory:
    1) explicit `version` arg, or
    2) env RDCDM_VERSION, or
    3) pyproject version, or
    4) latest directory found by scanning.
    """
    # repo root: rd_cdm/util/versioning.py -> .../src/rd_cdm/util -> up 2
    root = Path(__file__).resolve().parents[2]
    base = root / "rd_cdm" / "instances"

    # 1/2/3: choose version
    chosen_version = (
        version
        or os.getenv("RDCDM_VERSION")
        or _read_project_version(root / "pyproject.toml")
    )

    # 3a) Use chosen version if present
    if chosen_version:
        vtag = version_to_tag(chosen_version)
        candidate = base / vtag
        if candidate.is_dir():
            return candidate

    # 4) Fallback: pick latest by scanning
    try:
        from packaging.version import Version
    except Exception:
        Version = None  # type: ignore

    best = None
    for d in base.iterdir():
        if d.is_dir():
            norm = normalize_dir_to_version(d.name)
            if not norm:
                continue
            if Version:
                try:
                    key = Version(norm)
                except Exception:
                    continue
            else:
                key = tuple(int(x) for x in norm.split("."))  # naive fallback
            if not best or key > best[0]:
                best = (key, d)

    if best:
        return best[1]

    raise FileNotFoundError(f"No instances directory found in {base}")
