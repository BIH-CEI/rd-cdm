import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from src.data_model.codesystems import create_code_systems

# Define the versions for each code system
versions = {
    "NCBITaxon": "2024-07-03",
    "GENO": "2023-10-08",
    "SO": "2.6",
    "ICD10CM": "2024-09-01",
    "SNOMED": "2024-09-01",
    "ICD11": "2024-09-01",
    "HL7FHIR": "v4.0.1",
    "GA4GH": "v2.0",
    "ISO3166": "2020(en)",
    "ICF": "1.0.2",
    "MONDO": "2024-09-03",
    "ORPHA": "2024-09-12",
    "OMIM": "2024-09-12",
    "LOINC": "2.78",
    "HGVS": "21.0.0",
    "HGNC": "2024-08-23",
    "HP": "2024-08-13",
    "NCIT": "24.04e"
}

# Create the code systems, but only include those with defined versions
code_systems = create_code_systems(versions)

# Define a function to create the JSON structure
def create_codesystem_json():
    code_systems_json = {
        "CodeSystems": [
            {
                "codeSystemName": cs.name,
                "namespace_prefix": cs.namespace_prefix,
                "version": versions[cs.namespace_prefix],  # Use the dynamically defined version
                "url": cs.url,
                "synonyms": cs.synonyms
            } for cs in code_systems
        ]
    }

    # Write to JSON file
    with open("rd_cdm_codesystems_v2_0_0.json", "w") as json_file:
        json.dump(code_systems_json, json_file, indent=2)
        print("JSON file created successfully: rd_cdm_codesystems_v2_0_0.json")

# Run the function
if __name__ == "__main__":
    create_codesystem_json()
