"""The instance data must project cleanly into a documentable LinkML schema.

`rd-cdm-profile` turns the value sets into enums and the data elements into
slots so that stock `gen-doc` can render them. Both directions can break: a
duplicate value set label collapses two enums onto one name, a post-coordinated
SNOMED expression is not a CURIE and cannot be a `slot_uri`, and the `section`
labels are not consistent enough to group on.
"""
from __future__ import annotations

from pathlib import Path

import pytest
import ruamel.yaml

from rd_cdm.utils.gen_profile import _group_key, _section_label, _slot_name, build

REPO_ROOT = Path(__file__).resolve().parents[1]
INSTANCES = REPO_ROOT / "src" / "rd_cdm" / "instances"


def _load(name: str) -> dict:
    yaml = ruamel.yaml.YAML(typ="safe")
    with (INSTANCES / name).open("r", encoding="utf-8") as fh:
        return yaml.load(fh) or {}


@pytest.fixture(scope="module")
def profile() -> dict:
    merged = {
        "code_systems": _load("code_systems.yaml").get("code_systems", []),
        "data_elements": _load("data_elements.yaml").get("data_elements", []),
        "value_sets": _load("value_sets.yaml").get("value_sets", []),
    }
    return build(merged, version="test", date="2026-01-01")


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def test_section_labels_lose_their_ordinal():
    assert _section_label("6.4 Family History") == "Family History"
    assert _section_label("1. Formal Criteria") == "Formal Criteria"
    assert _section_label("") == "Unsectioned"


def test_slot_names_are_filename_and_link_safe():
    # A slash lands in the file path; brackets break Markdown link syntax.
    assert _slot_name("6.4.2", "Propositus/-a") == "6.4.2 Propositus-a"
    assert (
        _slot_name("6.1.14", "Clinical Significance [ACMG]")
        == "6.1.14 Clinical Significance ACMG"
    )
    assert _slot_name("2.2", "Sex at Birth") == "2.2 Sex at Birth"


def test_no_slot_name_contains_a_path_or_link_breaker(profile):
    for name in profile["slots"]:
        assert not set(name) & set('\\/[]<>:"\'|?*#'), name


def test_the_untouched_element_name_survives_as_the_title(profile):
    # gen-doc renders the title as the page heading, so the real name is shown
    # even where the slot name had to be sanitised.
    assert profile["slots"]["6.4.2 Propositus-a"]["title"] == "6.4.2 Propositus/-a"


def test_grouping_is_by_ordinal_not_section():
    # 6.4.0-6.4.5 say "6.4 Family History" and 6.4.6-6.4.13 say "6.4 Family";
    # grouping on the label would split one section into two classes.
    assert _group_key("6.4.0") == _group_key("6.4.13") == "6.4"
    assert _group_key("2.2") == "2"
    assert _group_key("6.1.16") == "6.1"


# --------------------------------------------------------------------------- #
# The shipped model
# --------------------------------------------------------------------------- #

def test_every_value_set_becomes_an_enum(profile):
    declared = _load("value_sets.yaml").get("value_sets", [])
    assert len(profile["enums"]) == len(declared)


def test_every_data_element_becomes_a_slot(profile):
    declared = _load("data_elements.yaml").get("data_elements", [])
    assert len(profile["slots"]) == len(declared)


def test_slot_names_carry_the_ordinal(profile):
    assert "2.2 Sex at Birth" in profile["slots"]
    # 5.9 and 6.2.7 are both called "Severity"; the ordinal is what keeps them
    # apart, which is why no section prefix is needed.
    assert "5.9 Severity" in profile["slots"]
    assert "6.2.7 Severity" in profile["slots"]


def test_family_history_is_one_class_not_two(profile):
    assert "FamilyHistory" in profile["classes"]
    assert "Family" not in profile["classes"]


def test_post_coordinated_codes_are_not_slot_uris(profile):
    """6.2.3's element code is a SNOMED expression, not a CURIE."""
    slot = profile["slots"]["6.2.3 Determination Date"]
    assert "slot_uri" not in slot
    assert "=" in slot["annotations"]["element_code"]


def test_coded_elements_range_on_their_value_set(profile):
    assert profile["slots"]["2.2 Sex at Birth"]["range"] == "SexAtBirthValueSet"
    assert profile["slots"]["3.1 Vital Status"]["range"] == "VitalStatusValueSet"


def test_inactive_codes_are_deprecated_and_name_their_successor(profile):
    pvs = profile["enums"]["SexAtBirthValueSet"]["permissible_values"]
    inactive = pvs["SNOMEDCT:184115007"]
    assert inactive["deprecated"]
    assert "SNOMEDCT:261665006" in inactive["description"]
    # the successor must be a member of the same enum, or a stored value could
    # not be migrated without leaving the value set
    assert "SNOMEDCT:261665006" in pvs


def test_display_labels_survive_as_titles(profile):
    pvs = profile["enums"]["KaryotypicSexValueSet"]["permissible_values"]
    assert pvs["SNOMEDCT:734875008"]["title"] == "XX"
    assert pvs["SNOMEDCT:734875008"]["description"] == "Karyotype 46, XX"


def test_the_profile_loads_as_a_schema_definition(profile, tmp_path):
    linkml_runtime = pytest.importorskip("linkml_runtime")  # noqa: F841
    from linkml_runtime.linkml_model.meta import SchemaDefinition
    from linkml_runtime.loaders import yaml_loader

    path = tmp_path / "rd_cdm_profile.yaml"
    yaml = ruamel.yaml.YAML()
    with path.open("w", encoding="utf-8") as fh:
        yaml.dump(profile, fh)

    schema = yaml_loader.load(str(path), SchemaDefinition)
    assert schema.name == "rd-cdm-profile"
    assert len(schema.enums) == len(profile["enums"])
    assert len(schema.slots) == len(profile["slots"])
