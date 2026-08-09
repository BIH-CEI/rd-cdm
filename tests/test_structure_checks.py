"""Structural consistency of the shipped model, and of the checker itself.

These run without a BioPortal key, which is the point: the defects they catch
(a value set declared twice, a data element pointing at a value set that does
not exist, a value set id left behind when its data element was recoded) are
invisible to the BioPortal pass and were previously invisible to CI.
"""
from __future__ import annotations

from pathlib import Path

import ruamel.yaml

from rd_cdm.utils.structure_checks import check_structure

REPO_ROOT = Path(__file__).resolve().parents[1]
INSTANCES = REPO_ROOT / "src" / "rd_cdm" / "instances"


def _load(name: str) -> dict:
    yaml = ruamel.yaml.YAML(typ="safe")
    with (INSTANCES / name).open("r", encoding="utf-8") as fh:
        return yaml.load(fh) or {}


def _shipped_model() -> dict:
    """Assemble from the part files, so this does not depend on a fresh merge."""
    return {
        "code_systems": _load("code_systems.yaml").get("code_systems", []),
        "data_elements": _load("data_elements.yaml").get("data_elements", []),
        "value_sets": _load("value_sets.yaml").get("value_sets", []),
    }


# --------------------------------------------------------------------------- #
# The shipped model
# --------------------------------------------------------------------------- #

def test_shipped_model_is_structurally_consistent():
    problems = check_structure(_shipped_model())
    assert problems == [], "structural problems:\n" + "\n".join(f"  - {p}" for p in problems)


def test_every_inactive_code_explains_itself_and_names_a_successor():
    for vs in _shipped_model()["value_sets"]:
        members = {
            f"{c['system']}:{c['code']}"
            for c in vs.get("codes", []) or []
            if isinstance(c, dict)
        }
        for code in vs.get("codes", []) or []:
            if not isinstance(code, dict) or code.get("status") != "inactive":
                continue
            curie = f"{code['system']}:{code['code']}"
            assert code.get("statusNote"), (
                f"{vs['id']}: {curie} is inactive without a statusNote"
            )
            successor = code.get("replacedBy")
            assert successor, (
                f"{vs['id']}: {curie} is inactive without a replacedBy, so a "
                "stored value has nowhere to migrate to"
            )
            assert successor in members, (
                f"{vs['id']}: {curie} is replaced by {successor}, which is not a "
                "member of the same value set"
            )


# --------------------------------------------------------------------------- #
# The checker
# --------------------------------------------------------------------------- #

def _model(value_sets, data_elements, code_systems=None):
    return {
        "code_systems": code_systems if code_systems is not None else [{"id": "SNOMEDCT"}],
        "data_elements": data_elements,
        "value_sets": value_sets,
    }


def _de(ordinal, name, system, code, value_set=None):
    return {
        "ordinal": ordinal,
        "elementName": name,
        "elementCode": {"system": system, "code": code},
        "valueSet": value_set,
    }


def test_clean_model_has_no_problems():
    model = _model(
        value_sets=[{
            "id": "SNOMEDCT:1",
            "label": "VS A",
            "codes": [{"system": "SNOMEDCT", "code": "10", "label": "Ten"}],
        }],
        data_elements=[_de("1.1", "A", "SNOMEDCT", "1", "VS A")],
    )
    assert check_structure(model) == []


def test_duplicate_value_set_id_is_reported():
    vs = {"id": "SNOMEDCT:1", "label": "VS A", "codes": []}
    model = _model(
        value_sets=[vs, dict(vs)],
        data_elements=[_de("1.1", "A", "SNOMEDCT", "1", "VS A")],
    )
    assert any("declared 2 times" in p for p in check_structure(model))


def test_duplicate_value_set_label_is_reported():
    model = _model(
        value_sets=[
            {"id": "SNOMEDCT:1", "label": "Severity", "codes": []},
            {"id": "HP:2", "label": "Severity", "codes": []},
        ],
        data_elements=[
            _de("1.1", "A", "SNOMEDCT", "1", "Severity"),
            _de("1.2", "B", "HP", "2", "Severity"),
        ],
        code_systems=[{"id": "SNOMEDCT"}, {"id": "HP"}],
    )
    assert any("is used by 2 value sets" in p for p in check_structure(model))


def test_stale_value_set_id_is_reported():
    """The Sex at Birth case: the element moved to LOINC, the id did not."""
    model = _model(
        value_sets=[{"id": "SNOMEDCT:281053000", "label": "Sex at Birth", "codes": []}],
        data_elements=[_de("2.2", "Sex at Birth", "LOINC", "76689-9", "Sex at Birth")],
        code_systems=[{"id": "SNOMEDCT"}, {"id": "LOINC"}],
    )
    assert any("does not match the element code" in p for p in check_structure(model))


def test_missing_value_set_is_reported():
    model = _model(
        value_sets=[],
        data_elements=[_de("1.1", "A", "SNOMEDCT", "1", "VS A")],
    )
    assert any("which is not declared" in p for p in check_structure(model))


def test_unreferenced_value_set_is_reported():
    model = _model(
        value_sets=[{"id": "SNOMEDCT:1", "label": "VS A", "codes": []}],
        data_elements=[_de("1.1", "A", "SNOMEDCT", "1", None)],
    )
    assert any("no data element uses it" in p for p in check_structure(model))


def test_value_set_placeholders_are_not_references():
    model = _model(
        value_sets=[],
        data_elements=[
            _de("1.1", "A", "SNOMEDCT", "1", None),
            _de("1.2", "B", "SNOMEDCT", "2", "n/a"),
            _de("1.3", "C", "SNOMEDCT", "3", ""),
        ],
    )
    assert check_structure(model) == []


def test_duplicate_member_within_a_value_set_is_reported():
    model = _model(
        value_sets=[{
            "id": "SNOMEDCT:1",
            "label": "VS A",
            "codes": [
                {"system": "SNOMEDCT", "code": "10"},
                {"system": "SNOMEDCT", "code": "10"},
            ],
        }],
        data_elements=[_de("1.1", "A", "SNOMEDCT", "1", "VS A")],
    )
    assert any("is listed 2 times" in p for p in check_structure(model))


def test_inactive_member_without_a_note_is_reported():
    model = _model(
        value_sets=[{
            "id": "SNOMEDCT:1",
            "label": "VS A",
            "codes": [
                {"system": "SNOMEDCT", "code": "10", "status": "inactive"},
                {"system": "SNOMEDCT", "code": "11"},
            ],
        }],
        data_elements=[_de("1.1", "A", "SNOMEDCT", "1", "VS A")],
    )
    assert any("no statusNote" in p for p in check_structure(model))


def test_successor_outside_the_value_set_is_reported():
    model = _model(
        value_sets=[{
            "id": "SNOMEDCT:1",
            "label": "VS A",
            "codes": [
                {
                    "system": "SNOMEDCT", "code": "10", "status": "inactive",
                    "statusNote": "gone", "replacedBy": "SNOMEDCT:99",
                },
                {"system": "SNOMEDCT", "code": "11"},
            ],
        }],
        data_elements=[_de("1.1", "A", "SNOMEDCT", "1", "VS A")],
    )
    assert any("not a member of this value set" in p for p in check_structure(model))


def test_successor_on_an_active_code_is_reported():
    model = _model(
        value_sets=[{
            "id": "SNOMEDCT:1",
            "label": "VS A",
            "codes": [
                {"system": "SNOMEDCT", "code": "10", "replacedBy": "SNOMEDCT:11"},
                {"system": "SNOMEDCT", "code": "11"},
            ],
        }],
        data_elements=[_de("1.1", "A", "SNOMEDCT", "1", "VS A")],
    )
    assert any("but is not marked inactive" in p for p in check_structure(model))


def test_all_inactive_value_set_is_reported():
    model = _model(
        value_sets=[{
            "id": "SNOMEDCT:1",
            "label": "VS A",
            "codes": [{
                "system": "SNOMEDCT", "code": "10",
                "status": "inactive", "statusNote": "gone",
            }],
        }],
        data_elements=[_de("1.1", "A", "SNOMEDCT", "1", "VS A")],
    )
    assert any("every member is inactive" in p for p in check_structure(model))


def test_undeclared_code_system_is_reported():
    model = _model(
        value_sets=[{
            "id": "SNOMEDCT:1",
            "label": "VS A",
            "codes": [{"system": "MADEUP", "code": "10"}],
        }],
        data_elements=[_de("1.1", "A", "SNOMEDCT", "1", "VS A")],
    )
    assert any("not declared in code_systems.yaml" in p for p in check_structure(model))
