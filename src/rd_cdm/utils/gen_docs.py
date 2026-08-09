#!/usr/bin/env python3
"""Generate browsable LinkML documentation for the RD-CDM schema.

Runs LinkML's ``gen-doc`` over ``schema/rd_cdm.yaml`` and writes Markdown into
``docs/datamodel/``, where Sphinx renders it via myst-parser. Regenerate after
any schema change:

    poetry run rd-cdm-docs
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from rd_cdm.utils.versioning import get_model_version, schema_path

REPO_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_DIR = REPO_ROOT / "docs" / "datamodel"
REFERENCE_DIR = REPO_ROOT / "docs" / "reference"
PROFILE_SCHEMA = "rd_cdm_profile.yaml"

#: Pages gen-doc emits that nothing links to and that carry no information:
#: a schema stub whose body is literally "None", and a types index that is empty
#: once the LinkML builtins are excluded.
ORPHAN_PAGES = ("rd-cdm.md", "rd-cdm-profile.md", "types.md")

INDEX_HEADER = """# Data Model Reference

Generated from `schema/rd_cdm.yaml` (RD-CDM {version}) with LinkML `gen-doc`.
Do not edit these files by hand — run `rd-cdm-docs` after changing the schema.

This documents the *container*: the classes an RD-CDM document is built from.
For the data elements and value sets themselves, see the
[Element Reference](../reference/index.md).

"""

REFERENCE_HEADER = """# Element Reference

Generated from the RD-CDM instance data (RD-CDM {version}) via `rd-cdm-profile`
and LinkML `gen-doc`. Do not edit these files by hand — run
`rd-cdm-profile && rd-cdm-docs`.

Each section is a class, each data element a slot named by its ordinal, and each
value set an enumeration listing every permitted code with its CURIE. Codes
marked **DEPRECATED** do not resolve against BioPortal and are not available for
new data capture; their description names the code to use instead.

For the container schema these are instances of, see the
[Data Model Reference](../datamodel/index.md).

"""


def _render(schema: Path, directory: Path, header: str) -> int:
    """Run stock gen-doc over one schema and prepend provenance to its index."""
    if directory.exists():
        shutil.rmtree(directory)
    directory.mkdir(parents=True)

    subprocess.run(
        [
            "gen-doc",
            str(schema),
            "--directory",
            str(directory),
            # Without this, gen-doc documents every LinkML builtin type -
            # String, Boolean, Jsonpointer, Sparqlpath and 15 others, of which
            # the schema uses four. Nineteen pages of metamodel boilerplate
            # carrying nothing about the RD-CDM.
            "--no-mergeimports",
        ],
        check=True,
    )

    for name in ORPHAN_PAGES:
        (directory / name).unlink(missing_ok=True)

    index = directory / "index.md"
    if index.exists():
        body = index.read_text(encoding="utf-8")
        index.write_text(
            header.format(version=get_model_version() or "unknown") + body,
            encoding="utf-8",
        )

    return len(list(directory.glob("*.md")))


def main() -> None:
    schema = schema_path()
    if not schema.exists():
        sys.exit(f"ERROR: schema not found at {schema}")

    profile = schema.parent / PROFILE_SCHEMA
    if not profile.exists():
        sys.exit(
            f"ERROR: {PROFILE_SCHEMA} not found at {profile}.\n"
            "  Run rd-cdm-profile first."
        )

    if shutil.which("gen-doc") is None:
        sys.exit(
            "ERROR: gen-doc not found. Install the dev extra:\n"
            "  poetry install -E dev"
        )

    n_model = _render(schema, OUTPUT_DIR, INDEX_HEADER)
    print(f"Wrote {n_model} page(s) to {OUTPUT_DIR}")

    n_ref = _render(profile, REFERENCE_DIR, REFERENCE_HEADER)
    print(f"Wrote {n_ref} page(s) to {REFERENCE_DIR}")


if __name__ == "__main__":
    main()
