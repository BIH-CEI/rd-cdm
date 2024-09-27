import jsonschema
import json
import os

def validate_schemas(version):
    # Construct the base path and version-specific file paths
    base_path = f'rd-cdm/res/v{version}/'
    
    schema_file = f'{base_path}schema_v{version}.json'
    data_elements_file = f'{base_path}data_elements_v{version}.json'
    codesystems_file = f'{base_path}codesystems_v{version}.json'
    value_sets_file = f'{base_path}value_sets_v{version}.json'

    # Load the main schema
    with open(schema_file) as schema_file:
        schema = json.load(schema_file)

    # Validate each JSON file against the schema
    for file in [data_elements_file, codesystems_file, value_sets_file]:
        with open(file) as json_file:
            data = json.load(json_file)
            try:
                jsonschema.validate(instance=data, schema=schema)
            except jsonschema.ValidationError as e:
                print(f"Validation error in {file}: {e.message}")
                return False

    print(f"All schemas for version {version} are valid.")
    return True