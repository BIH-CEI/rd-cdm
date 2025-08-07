"""
RD-CDM tests package.

This package contains unit tests for the RD-CDM library, covering:

- **CSV parsing and export** (`test_csv_parsing.py`):
  Verifies that all part YAML files (`code_systems.yaml`, `data_elements.yaml`, 
  `value_sets.yaml`) are correctly converted to individual CSVs and that a 
  combined `rd_cdm_vX_Y_Z.csv` is generated.

- **JSON parsing and export** (`test_json_parsing.py`):
  Checks that part YAMLs are converted to individual JSON files, skipping the 
  pre-merged `rd_cdm_vX_Y_Z.yaml` in the loop, and ensuring the combined 
  `rd_cdm_vX_Y_Z.json` is created at the end.

- **Instance merging** (`test_merge_instances.py`):
  Tests that versioned instance parts are merged into a single 
  `rd_cdm_vX_Y_Z.yaml` file.

- **Validation utilities** (`test_validation_utils.py`):
  Ensures helper functions for code cleaning, ontology label fetching, 
  and version retrieval work as expected.

- **Version resolution** (`test_versioning.py`):
  Validates that `resolve_instances_dir` and related helpers correctly locate 
  and normalize the target instances directory for a given version.

All tests use `pytest` and rely on temporary directories or monkeypatching to 
avoid altering the actual RD-CDM source data.
"""

__all__ = []
