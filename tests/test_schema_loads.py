"""The schema must load as a LinkML SchemaDefinition.

An unrecognised top-level key does not break `rd-cdm-merge`, which reads the
schema as plain YAML, but it makes `linkml validate` and `gen-doc` fail before
they do any work. A top-level `date:` did exactly that, and went unnoticed
because the CI job that runs `linkml validate` was failing at its install step.
"""
from __future__ import annotations

import pytest

from rd_cdm.utils.versioning import get_model_date, get_model_version, schema_path

linkml_runtime = pytest.importorskip("linkml_runtime")


def _load():
    from linkml_runtime.linkml_model.meta import SchemaDefinition
    from linkml_runtime.loaders import yaml_loader

    return yaml_loader.load(str(schema_path()), SchemaDefinition)


def test_schema_loads_as_a_schema_definition():
    schema = _load()
    assert schema.name
    assert schema.version == get_model_version()


def test_release_date_is_an_annotation_not_a_top_level_key():
    schema = _load()
    date = get_model_date()
    assert date, "annotations.rd_cdm_date is missing from the schema"
    assert str(schema.annotations["rd_cdm_date"].value) == date


def test_code_status_enum_is_declared():
    schema = _load()
    assert "CodeStatus" in schema.enums
    assert set(schema.enums["CodeStatus"].permissible_values) == {"active", "inactive"}


def test_coding_carries_the_provenance_attributes():
    schema = _load()
    attributes = set(schema.classes["Coding"].attributes)
    assert {"displayLabel", "status", "replacedBy", "statusNote"} <= attributes
