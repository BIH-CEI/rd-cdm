import json
import sys
import os
import importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.data_model.codesystems import create_code_systems


def load_code_system_versions(version):
    """
    Load code system versions for the specified data model version.

    This function dynamically imports a Python module that holds the versioned
    code systems for a given data model version (e.g., "v2_0_0"). Each version
    is stored in a class containing a dictionary mapping code system names to
    their respective version numbers.

    The module to be imported should follow a standard structure:
    - The module is located in "src/<version>/" (e.g., "src/v2_0_0/").
    - It contains a class named "CODESYSTEMS_VERSIONS_<version>" that stores 
      the code system versions in a dictionary called `versions`.
    
    Example:
    - For version "v2_0_0", the module "rd_cdm_v2_0_0_codesystems_versions.py" 
      should define a class "CODESYSTEMS_VERSIONS_V2_0_0" containing a `versions`
      dictionary with code system mappings.

    :param version: A string representing the version of the code systems 
                    to load (e.g., "v2_0_0").
    :return: A dictionary with the code system versions for the given version, 
             or None if the module or class is not found.
    """
    try:
        module = importlib.import_module(
            f"src.{version}.rd_cdm_{version}_codesystems_versions"
        )
        class_name = f"CODESYSTEMS_VERSIONS_{version.replace('.', '_').upper()}"
        version_class = getattr(module, class_name)
        return version_class.versions 
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error loading version module for {version}: {e}")
        return None

def create_codesystem_json(version):
    """
    Create a JSON file for the code systems of a specified version.

    This function generates a JSON file containing the code systems for a 
    given version of the data model. It first loads the code system versions 
    using `load_code_system_versions()`, then it uses `create_code_systems()` 
    to build a list of code systems. The result is written as a JSON file in 
    the "res" folder under the respective version directory.

    Example:
    - For version "v2_0_0", the JSON will be created at:
      "res/v2_0_0/rd_cdm_codesystems_v2_0_0.json".

    :param version: A string representing the data model version (e.g., 
                    "v2_0_0").
    """

    versions = load_code_system_versions(version)
    if versions is None:
        print(f"Failed to create code system JSON for {version}.")
        return

    code_systems = create_code_systems(versions)

    code_systems_json = {
        "CodeSystems": [
            {
                "codeSystemName": cs.name,
                "namespace_prefix": cs.namespace_prefix,
                "version": versions[cs.namespace_prefix],
                "url": cs.url,
                "synonyms": cs.synonyms
            } for cs in code_systems if cs.namespace_prefix in versions
        ]
    }

    output_path = f"res/{version}/rd_cdm_codesystems_{version}.json"
    with open(output_path, "w") as json_file:
        json.dump(code_systems_json, json_file, indent=2)
        print(f"JSON file created successfully: {output_path}")

if __name__ == "__main__":
    create_codesystem_json("v2_0_0")

