import json
import sys
import os
import importlib

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from data_model.utils import json_serializer
from src.data_model.value_set import ValueSet, ValueSetChoice
from src.data_model.base_types import Coding, CodeSystem

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
        module = importlib.import_module(f"src.{version}.rd_cdm_{version}_codesystems_versions")
        class_name = f"CODESYSTEMS_VERSIONS_{version.replace('.', '_').upper()}"
        version_class = getattr(module, class_name)
        return version_class.versions
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error loading code system version module for {version}: {e}")
        return {}

import os
import json
from data_model.utils import json_serializer

def create_value_set_json(version):
    """Create a JSON file for the value sets of a specified version."""
    
    # Load value sets for the specified version
    value_sets = load_value_set_definitions(version)
    if value_sets is None:
        print(f"Failed to create value set JSON for {version}.")
        return

    # Load code system versions for the specified version
    code_system_versions = load_code_system_versions(version)
    
    # Create a JSON structure for the value sets
    value_sets_json = {
        "version": version,
        "dataElements": [],  # Add dataElements as required by schema
        "valueSets": [
            {
                "valueSetName": vs.valueSetName,
                "valueSetOrigin": vs.valueSetOrigin,
                "valueSetLink": vs.valueSetLink,
                "display": vs.display,
                "valueSetCode": vs.valueSetCode.code if isinstance(
                    vs.valueSetCode, Coding) else None,
                
                "valueSetCodeSystem": [
                    {
                        "codeSystem": system.namespace_prefix,
                        "version": code_system_versions.get(
                            system.namespace_prefix, "unknown")
                    }
                    for system in vs.valueSetCodeSystem if isinstance(
                        vs.valueSetCodeSystem, list)
                ] if isinstance(vs.valueSetCodeSystem, list) else [
                    {
                        "codeSystem": vs.valueSetCodeSystem.namespace_prefix,
                        "version": code_system_versions.get(
                            vs.valueSetCodeSystem.namespace_prefix, "unknown")
                    }
                ] if isinstance(vs.valueSetCodeSystem, CodeSystem) else None,
                
                "valueSetChoices": [
                    {
                        "choiceDisplay": choice.choiceDisplay,
                        "choiceCode": choice.choiceCode.code if isinstance(
                            choice.choiceCode, Coding) else None,
                        "choiceCodeSystem": 
                            choice.choiceCodeSystem.namespace_prefix if 
                                isinstance(choice.choiceCodeSystem, CodeSystem)
                                    else None,
                        "choiceCodeSystemVersion": code_system_versions.get(
                            choice.choiceCodeSystem.namespace_prefix, "unknown"
                        ) if isinstance(choice.choiceCodeSystem, CodeSystem) 
                            else "unknown"
                    }
                    for choice in vs.valueSetChoices
                ]
            }
            for vs in value_sets
        ]
    }

    # Ensure the output directory exists
    output_directory = f"res/{version}/"
    os.makedirs(output_directory, exist_ok=True)

    # Write the JSON file to the res folder
    output_path = os.path.join(output_directory, f"rd_cdm_value_sets_{version}.json")
    with open(output_path, "w") as json_file:
        json.dump(value_sets_json, json_file, default=json_serializer, indent=2)
        print(f"JSON file created successfully: {output_path}")


# Example usage
if __name__ == "__main__":
    create_value_set_json("v2_0_0")
