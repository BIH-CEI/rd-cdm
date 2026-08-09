"""Serve the schema, instances and exports as downloads from the built site.

Those files live in ``src/rd_cdm/`` and ``res/``, outside ``docs_dir``, and
MkDocs only serves what is inside it. Copying them into ``docs/`` permanently
would put generated artefacts under version control twice, so they are attached
to the build instead: the site gets current files on every build and git keeps
one copy.

Each entry declares its destination explicitly rather than reusing the source
filename, because ``schema/rd_cdm.yaml`` and ``instances/rd_cdm.yaml`` are
different files with the same name. Destinations are ``docs_dir``-relative URIs
so that MkDocs' link validation resolves ``../downloads/...`` against them.

Referenced from ``mkdocs.yml`` under ``hooks:``.
"""
from __future__ import annotations

import logging
from pathlib import Path

from mkdocs.structure.files import File

log = logging.getLogger("mkdocs.hooks.copy_downloads")

#: {destination URI inside the site: source path relative to the repo root}
DOWNLOADS = {
    # Schema
    "downloads/rd_cdm_schema.yaml": "src/rd_cdm/schema/rd_cdm.yaml",
    "downloads/rd_cdm_profile.yaml": "src/rd_cdm/schema/rd_cdm_profile.yaml",
    # Merged instance and exports
    "downloads/rd_cdm.yaml": "src/rd_cdm/instances/rd_cdm.yaml",
    "downloads/rd_cdm.json": "src/rd_cdm/instances/jsons/rd_cdm.json",
    "downloads/rd_cdm.csv": "src/rd_cdm/instances/csvs/rd_cdm.csv",
    # Individual components
    "downloads/code_systems.yaml": "src/rd_cdm/instances/code_systems.yaml",
    "downloads/code_systems.json": "src/rd_cdm/instances/jsons/code_systems.json",
    "downloads/code_systems.csv": "src/rd_cdm/instances/csvs/code_systems.csv",
    "downloads/data_elements.yaml": "src/rd_cdm/instances/data_elements.yaml",
    "downloads/data_elements.json": "src/rd_cdm/instances/jsons/data_elements.json",
    "downloads/data_elements.csv": "src/rd_cdm/instances/csvs/data_elements.csv",
    "downloads/value_sets.yaml": "src/rd_cdm/instances/value_sets.yaml",
    "downloads/value_sets.json": "src/rd_cdm/instances/jsons/value_sets.json",
    "downloads/value_sets.csv": "src/rd_cdm/instances/csvs/value_sets.csv",
    # v2.0.0 archive
    "downloads/rd_cdm_v2_0_0.json": "res/v2_0_0/rd_cdm_v2_0_0.json",
    "downloads/rd_cdm_codesystems_v2_0_0.json": "res/v2_0_0/rd_cdm_codesystems_v2_0_0.json",
    "downloads/rd_cdm_data_elements_v2_0_0.json": "res/v2_0_0/rd_cdm_data_elements_v2_0_0.json",
    "downloads/rd_cdm_value_sets_v2_0_0.json": "res/v2_0_0/rd_cdm_value_sets_v2_0_0.json",
    "downloads/rd_cdm_v2_0_0.csv": "res/v2_0_0/rd_cdm_v2_0_0.csv",
    "downloads/rd_cdm_codesystems_v2_0_0.csv": "res/v2_0_0/rd_cdm_codesystems_v2_0_0.csv",
    "downloads/rd_cdm_data_elements_v2_0_0.csv": "res/v2_0_0/rd_cdm_data_elements_v2_0_0.csv",
    "downloads/rd_cdm_value_sets_v2_0_0.csv": "res/v2_0_0/rd_cdm_value_sets_v2_0_0.csv",
}


def on_files(files, config):
    repo_root = Path(config["config_file_path"]).parent
    attached = missing = 0

    for dest_uri, relative in DOWNLOADS.items():
        source = repo_root / relative
        if not source.exists():
            log.warning(
                "download not found, skipping %s (run rd-cdm-merge / "
                "rd-cdm-profile / rd-cdm-json / rd-cdm-csv): %s",
                dest_uri,
                relative,
            )
            missing += 1
            continue
        files.append(
            File.generated(config, dest_uri, abs_src_path=str(source))
        )
        attached += 1

    log.info("attached %d download(s), %d missing", attached, missing)
    return files
