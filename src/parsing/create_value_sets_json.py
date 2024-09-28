import json
import sys
import os
import importlib

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from data_model.utils import json_serializer
from src.data_model.value_set import ValueSet, ValueSetChoice

def load_value_set_definitions(version):
    """Dynamically load the value sets for a given version."""
    try:
        module = importlib.import_module(f"src.{version}.rd_cdm_{version}_value_sets")
        class_name = f"VALUE_SETS_VERSIONS_{version.replace('.', '_').upper()}"
        version_class = getattr(module, class_name)
        return version_class.value_sets
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error loading value set module for {version}: {e}")
        return None

def load_code_system_versions(version):
    """Dynamically load the code system versions for a given version."""
    try:
        # Dynamically load the code system version class
        module = importlib.import_module(f"src.{version}.rd_cdm_{version}_codesystems_versions")
        class_name = f"CODESYSTEMS_VERSIONS_{version.replace('.', '_').upper()}"
        version_class = getattr(module, class_name)
        
        # Ensure we're accessing the 'versions' dictionary directly
        return version_class.versions  # Access the dictionary directly
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error loading code system version module for {version}: {e}")
        return {}

# Example usage
code_system_versions = load_code_system_versions("v2_0_0")
print(code_system_versions.get("SNOMED", "unknown"))  # Should return '2024-09-01'

def create_value_set_json(version):
    value_sets = load_value_set_definitions(version)
    if value_sets is None:
        print(f"Failed to create value set JSON for {version}.")
        return

    # Create a JSON structure for the value sets
    value_sets_json = {
        "version": version,  # Add version to comply with schema
        "dataElements": [],  # Add dataElements as required by schema
        "valueSets": [
            {
                "valueSetName": vs.valueSetName,
                "valueSetOrigin": vs.valueSetOrigin,
                "valueSetLink": vs.valueSetLink,
                "display": vs.display,
                "valueSetCode": vs.valueSetCode.code,  # Assuming Coding object
                "valueSetCodeSystem": vs.valueSetCodeSystem.namespace_prefix,
                "valueSetCodeSystemVersion": code_system_versions.get(vs.valueSetCodeSystem.namespace_prefix, "unknown"),  # Fetch version dynamically
                "valueSetChoices": [
                    {
                        "choiceDisplay": choice.choiceDisplay,
                        "choiceCode": choice.choiceCode.code,
                        "choiceCodeSystem": choice.choiceCodeSystem.namespace_prefix,
                        "choiceCodeSystemVersion": code_system_versions.get(choice.choiceCodeSystem.namespace_prefix, "unknown")  # Fetch version dynamically
                    }
                    for choice in vs.valueSetChoices
                ]
            }
            for vs in value_sets
        ]
    }

    # Write the JSON file to the res folder
    output_path = f"res/{version}/rd_cdm_value_sets_{version}.json"
    with open(output_path, "w") as json_file:
        json.dump(value_sets_json, json_file, default=json_serializer, indent=2)
        print(f"JSON file created successfully: {output_path}")


if __name__ == "__main__":
    create_value_set_json("v2_0_0")
