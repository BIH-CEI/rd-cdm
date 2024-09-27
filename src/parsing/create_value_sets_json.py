import json
import sys
import os
import importlib

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.data_model.value_set import ValueSet, ValueSetChoice

def load_value_set_definitions(version):
    """Dynamically load the value sets for a given version."""
    try:
        # Dynamically import the module from the corresponding src version folder
        module = importlib.import_module(f"src.{version}.rd_cdm_{version}_value_sets")
        class_name = f"VALUE_SETS_VERSIONS_{version.replace('.', '_').upper()}"
        version_class = getattr(module, class_name)
        return version_class.value_sets  # Access the value sets list or dictionary
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error loading value set module for {version}: {e}")
        return None

def create_value_set_json(version):
    value_sets = load_value_set_definitions(version)
    if value_sets is None:
        print(f"Failed to create value set JSON for {version}.")
        return

    # Create a JSON structure for the value sets
    value_sets_json = {
        "valueSets": [
            {
                "valueSetName": vs.valueSetName,
                "valueSetOrigin": vs.valueSetOrigin,
                "valueSetLink": vs.valueSetLink,
                "display": vs.display,
                "valueSetCode": vs.valueSetCode.code,  # Assuming Coding object
                "valueSetCodeSystem": vs.valueSetCodeSystem.namespace_prefix,
                "valueSetChoices": [
                    {
                        "choiceDisplay": choice.choiceDisplay,
                        "choiceCode": choice.choiceCode.code,
                        "choiceCodeSystem": choice.choiceCodeSystem.namespace_prefix
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
        json.dump(value_sets_json, json_file, indent=2)
        print(f"JSON file created successfully: {output_path}")

# Run the function for the versions you want
if __name__ == "__main__":
    create_value_set_json("v2_0_0")
    # create_value_set_json("v2_1_0")
