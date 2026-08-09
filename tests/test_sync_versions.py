"""A placeholder version must never overwrite a real one.

BioPortal reports a non-version for some submissions - the 2026-08-08 run
replaced Sequence Ontology 2.6 with the string "unknown", losing information
that no later run could recover.
"""
from __future__ import annotations

from rd_cdm.utils.sync_versions import is_informative


def test_real_versions_are_informative():
    for version in ("2.6", "2025_09_01", "26.07d", "4.9", "v4.0.1", "281"):
        assert is_informative(version)


def test_placeholders_are_not_informative():
    for version in ("", "unknown", "<unknown>", "UNKNOWN", " none ", "null", None):
        assert not is_informative(version)
