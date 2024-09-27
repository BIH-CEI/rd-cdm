import json
import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_model import create_code_systems

# Function to dynamically load the versions from rd_cdm_v2_X_X_codesystems_versions.py for a given version
def load_code_system_versions(version):
    """Dynamically import the code system versions for a given version."""

    # Construct the module name for dynamic import
    version_module_path = f"res.{version}.rd_cdm_{version}_codesystems_versions"
    
    try:
        # Dynamically import the module using relative path
        module = importlib.import_module(f"res.{version}.rd_cdm_{version}_codesystems_versions", package='res')

        # Get the class name dynamically (like CODESYSTEMS_VERSIONS_V2_0_0)
        class_name = f"CODESYSTEMS_VERSIONS_{version.replace('.', '_').upper()}"
        
        # Get the class from the module
        versions_class = getattr(module, class_name)
        return versions_class.versions  # Return the versions from the class

    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error loading version module for {version}: {e}")
        return None


def create_codesystem_json(version):
    """Generate JSON for code systems for a specific version."""
    
    # Load the version-specific code system versions
    versions = load_code_system_versions(version)
    
    if versions is None:
        print(f"Failed to create code system JSON for {version}.")
        return
    
    # Create the code systems, filtering based on the versions defined
    code_systems = create_code_systems(versions)

    # Create the JSON structure
    code_systems_json = {
        "CodeSystems": [
            {
                "codeSystemName": cs.name,
                "namespace_prefix": cs.namespace_prefix,
                "version": versions[cs.namespace_prefix],
                "url": cs.url,
                "synonyms": cs.synonyms
            } for cs in code_systems
        ]
    }

    # Ensure the folder for the version exists
    version_folder = f"res/{version}"
    if not os.path.exists(version_folder):
        os.makedirs(version_folder)

    # Write the JSON to the correct versioned file
    json_file_path = f"{version_folder}/rd_cdm_codesystems_{version}.json"
    with open(json_file_path, "w") as json_file:
        json.dump(code_systems_json, json_file, indent=2)
        print(f"JSON file created successfully: {json_file_path}")


if __name__ == "__main__":
    create_codesystem_json("v2_0_0")

   # create_codesystem_json("v2_1_0")
