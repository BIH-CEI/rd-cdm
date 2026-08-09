#!/usr/bin/env python3
"""Sync code system versions in code_systems.yaml with BioPortal.

Only ``version:`` fields are touched. Label drift is deliberately left alone:
a changed label can mean a term was redefined or obsoleted, which needs a human
decision rather than a mechanical edit.
"""
from __future__ import annotations

import sys

import ruamel.yaml

from rd_cdm.utils.config import resolve_paths
from rd_cdm.utils.settings import ValidationSettings
from rd_cdm.utils.validation_utils import UNINFORMATIVE_VERSIONS, get_remote_version

SKIP = {"CustomCode", "GA4GH", "HL7FHIR", "HGVS", "ICD11", "ISO3166"}


def is_informative(version: str) -> bool:
    """Whether a version string is worth recording.

    BioPortal reports a placeholder for some submissions. Writing that over a
    real version loses information, so those are skipped rather than applied.
    """
    return bool(version) and str(version).strip().lower() not in UNINFORMATIVE_VERSIONS


def main() -> None:
    settings = ValidationSettings()
    if not settings.bioportal_api_key:
        print("ERROR: BIOPORTAL_API_KEY not set", file=sys.stderr)
        sys.exit(2)

    path = resolve_paths().instances_dir / "code_systems.yaml"
    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    with open(path, encoding="utf-8") as fh:
        doc = yaml.load(fh)

    changed, skipped = [], []
    for cs in doc.get("code_systems", []):
        cs_id = cs.get("id")
        if not cs_id or cs_id in SKIP:
            continue
        try:
            live = get_remote_version(cs_id)
        except Exception as exc:
            print(f"  ? {cs_id}: could not fetch live version ({exc})")
            continue
        current = cs.get("version", "")
        if live == current:
            continue
        if not is_informative(live):
            skipped.append((cs_id, current, live))
            continue
        cs["version"] = live
        changed.append((cs_id, current, live))

    for cs_id, current, live in skipped:
        print(
            f"  ! {cs_id}: BioPortal reports '{live}'; keeping '{current}' "
            "(placeholder versions are not applied)"
        )

    if not changed:
        print("No version drift.")
        return

    with open(path, "w", encoding="utf-8") as fh:
        yaml.dump(doc, fh)

    print(f"Updated {len(changed)} code system version(s):")
    for cs_id, old, new in changed:
        print(f"  {cs_id}: {old} -> {new}")


if __name__ == "__main__":
    main()
