import json
import pytest
from jsonschema import validate, ValidationError
import os

# Base directory where the res and schema folders are located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# List of JSON files to validate with corresponding schemas
# Path to the schema files
CODE_SYSTEMS_SCHEMA = "schemas/rd_cdm_code_systems_schema.json"
DATA_ELEMENTS_SCHEMA = "schemas/rd_cdm_data_elements_schema.json"
VALUE_SETS_SCHEMA = "schemas/rd_cdm_value_sets_schema.json"
FULL_MODEL_SCHEMA = "schemas/rd_cdm_v2_0_0_schema.json"

# List of JSON files and their corresponding schema
JSON_FILES_AND_SCHEMAS = [
    ("res/v2_0_0/rd_cdm_codesystems_v2_0_0.json", CODE_SYSTEMS_SCHEMA),
    ("res/v2_0_0/rd_cdm_data_elements_v2_0_0.json", DATA_ELEMENTS_SCHEMA),
    ("res/v2_0_0/rd_cdm_value_sets_v2_0_0.json", VALUE_SETS_SCHEMA),
    ("res/v2_0_0/rd_cdm_v2_0_0.json", FULL_MODEL_SCHEMA),
]

@pytest.mark.parametrize("json_file,schema_file", JSON_FILES_AND_SCHEMAS)
def test_validate_json_file(json_file, schema_file):
    """Validate JSON file against its corresponding schema."""
    try:
        with open(schema_file, "r") as sf:
            schema = json.load(sf)

        with open(json_file, "r") as jf:
            data = json.load(jf)

        validate(instance=data, schema=schema)
    except FileNotFoundError:
        pytest.fail(f"File not found: {json_file}")
    except json.JSONDecodeError as e:
        pytest.fail(f"Invalid JSON format in {json_file}: {e.msg}")
    except ValidationError as e:
        pytest.fail(f"Validation failed for {json_file}: {e.message}")
