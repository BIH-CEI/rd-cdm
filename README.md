# ontology-based rare disease common data model

Welcome to the repo of the ontology-based rare disease common data model (RD-CDM) harmonising international registry use, HL7® FHIR®, and the GA4GH Phenopacket Schema.

<!-- Badges -->
[![CI](https://github.com/BIH-CEI/rd-cdm/actions/workflows/ci.yml/badge.svg)](https://github.com/BIH-CEI/rd-cdm/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/rd-cdm/badge/?version=latest)](https://rd-cdm.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/863993011.svg)](https://doi.org/10.5281/zenodo.13891625)
![Python Versions](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12-blue)
[![PyPI](https://img.shields.io/pypi/v/rd-cdm.svg)](https://pypi.org/project/rd-cdm/)
[![Downloads](https://img.shields.io/pypi/dm/rd-cdm.svg?label=downloads)](https://pypi.org/project/rd-cdm/)
[![LinkML](https://img.shields.io/badge/LinkML-1.8.0+-green.svg)](https://linkml.io/)

**Latest docs:** https://rd-cdm.readthedocs.io/en/latest/

### Manuscript

The corresponding paper for RD-CDM v2.0.0 has been published in *Nature Scientific Data*:  
https://www.nature.com/articles/s41597-025-04558-z

---

## Table of Contents

- [Project Description](#project-description)
- [What you get from PyPI](#what-you-get-from-pypi)
- [Features](#features)
- [Installation](#installation)
  - [Quick start (pip)](#quick-start-pip)
  - [Development install](#development-install)
- [CLI tools](#cli-tools)
- [Versioning & File Layout](#versioning--file-layout)
- [Validating with BioPortal](#validating-with-bioportal)
- [Contributing & Contact](#contributing--contact)
- [Resources](#resources)
- [License](#license)
- [Citing](#citing)
- [Acknowledgements](#acknowledgements)

---

## Project Description

The ontology-based RD-CDM harmonizes rare disease data capture across registries. It integrates ERDRI-CDS, HL7 FHIR, and GA4GH Phenopacket Schema to support interoperable data for research and care. RD-CDM v2.0.x comprises 78 data elements covering formal criteria, personal information, patient status, disease, genetic findings, phenotypic findings, and family history.

---

## What you get from PyPI

Installing `rd-cdm` from PyPI provides:

- **Schema**
  - `src/rd_cdm/schema/rd_cdm.yaml`

- **Versioned instances (data packs)**
  - `src/rd_cdm/instances/v2_0_1/*.yaml` (e.g., `code_systems.yaml`, `data_elements.yaml`, `value_sets.yaml`)
  - merged file: `src/rd_cdm/instances/v2_0_1/rd_cdm_v2_0_1.yaml`
  - exports (if present or generated locally):
    - `src/rd_cdm/instances/v2_0_1/jsons/*.json`
    - `src/rd_cdm/instances/v2_0_1/csvs/*.csv`

- **Generated Python & Pydantic classes (LinkML)**
  - `src/rd_cdm/python_classes/rd_cdm.py` (LinkML runtime dataclasses)
  - `src/rd_cdm/python_classes/rd_cdm_pydantic.py` (generated from the schema via LinkML’s Pydantic generator)

- **Utilities / CLI entry points**
  - `rdcdm-merge` – merge instance parts into `rd_cdm_vX_Y_Z.yaml`
  - `rdcdm-json` – per-file JSON export + combined `rd_cdm_vX_Y_Z.json`
  - `rdcdm-csv` – per-file CSV export + combined `rd_cdm_vX_Y_Z.csv`
  - `rdcdm-validate` – validate ontology codes via BioPortal

---

## Features

- **Interoperability**: Aligns with HL7 FHIR v4.0.1 and GA4GH Phenopacket v2.0
- **Ontology-driven**: Uses SNOMED CT, LOINC, NCIT, MONDO, OMIM, HPO, and more
- **Modular**: Clear separation of schema, instances, and exports
- **Versioned data**: Instances shipped and resolved per version (e.g., `v2_0_1`)
- **Tooling**: Merge, export, and validation utilities with simple CLIs
- **(Optional) Pydantic models**: Strict runtime validation generated from LinkML

---

### Installation

From PyPI:

```bash
pip install rd-cdm
```

Optional extras for testing/docs:

```bash
pip install rd-cdm[test]     # pytest, etc.
# or
pip install rd-cdm[docs]
```

### Development install

```bash
git clone https://github.com/BIH-CEI/rd-cdm.git
cd rd-cdm
# (Recommended) create a venv
python -m venv .venv && source .venv/bin/activate
pip install -U pip
pip install -e .[test]
pytest -q
```

> We use a **src/** layout. If you run tools directly, ensure `PYTHONPATH=src` or use the installed CLI entry points shown below.

---

## CLI tools

After installation you should have these commands:

```bash
# Merge the versioned parts into rd_cdm_vX_Y_Z.yaml (auto-resolves latest if not given)
rdcdm-merge                  # or: rdcdm-merge --version 2.0.1

# Export JSON (per-file .json + combined rd_cdm_vX_Y_Z.json)
rdcdm-json                   # or: rdcdm-json -v 2.0.1

# Export CSV (per-file .csv + combined rd_cdm_vX_Y_Z.csv)
rdcdm-csv                    # or: rdcdm-csv -v 2.0.1

# Validate merged instance file against ontologies via BioPortal
rdcdm-validate               # or: rdcdm-validate -v 2.0.1 (Note: set up BioPortal API key for this)
```

### BioPoratal API Key Setup for Validation
The ``rdcdm-validate`` command uses the BioPortal API
to check ontology term validity. This requires an API key to be set as an environment variable.

#### Get an API key:

Sign up (or log in) at https://bioportal.bioontology.org/accounts/new

- Go to your account settings and copy your API Key.
- Set the API key in your environment

#### macOS / Linux (bash/zsh): 

```bash
export BIOPORTAL_API_KEY="your-key-here"
```

#### Windoes (PowerShell):
```bash
setx BIOPORTAL_API_KEY "your-key-here"
```

---

## Contributing and Contact

The RD-CDM is a community-driven effort and we invite open and international
collaboration. Please feel free to create issues, discuss features, 
or submit pull requests to help enhance this project. For larger contributions, 
consider reaching out to discuss collaboration opportunities. 
Please find more information on how to contact us and contribute 
in the [`Contribution` section of our documentation](https://rd-cdm.readthedocs.io/en/latest/contributing.html).

## RareLink 

RareLink is a novel rare disease framework in REDCap linking international 
registries, FHIR, and Phenopackets based on the RD-CDM. It is designed to 
support the collection of harmonized data for rare disease research 
across any REDCap project worldwide and allows for the preconfigured export of 
the RD-CDM data in FHIR and Phenopackets formats.

For more information on RareLink, please see the: 

- [RareLink Documentation](https://rarelink.readthedocs.io/en/latest/index.html)
- [RareLink GitHub](https://github.com/BIH-CEI/rarelink)

## Resources 

### Ontologies
- Human Phenotype Ontology [🔗](http://www.human-phenotype-ontology.org)
- Monarch Initiative Disease Ontology [🔗](https://mondo.monarchinitiative.org/)
- Online Mendelian Inheritance in Man [🔗](https://www.omim.org/)
- Orphanet Rare Disease Ontology [🔗](https://www.orpha.net/)
- SNOMED CT [🔗](https://www.snomed.org/snomed-ct)
- ICD 11 [🔗](https://icd.who.int/en)
- ICD10CM [🔗](https://www.cdc.gov/nchs/icd/icd10cm.htm)
- National Center for Biotechnology Information Taxonomy [🔗](https://www.ncbi.nlm.nih.gov/taxonomy)
- Logical Observation Identifiers Names and Codes [🔗](https://loinc.org/)
- HUGO Gene Nomenclature Committee [🔗](https://www.genenames.org/)
- Gene Ontology [🔗](https://geneontology.org/)
- NCI Thesaurus OBO Edition [🔗](https://obofoundry.org/ontology/ncit.html)

For the versions used in a specific RD-CDM version, please see the 
[resources in our documentation](https://rd-cdm.readthedocs.io/en/latest/resources/resources_file.html).

### Submodules
- [RareLink](https://github.com/BIH-CEI/RareLink)

## License

This project is licensed under the terms of the [MIT License](https://github.com/BIH-CEI/rd-cdm/blob/develop/LICENSE)

## Citing

If you use the model for your research, do not hesitate to reach out and 
please cite our article: 

> Graefe, A.S.L., Hübner, M.R., Rehburg, F. et al. An ontology-based rare disease common data model harmonising international registries, FHIR, and Phenopackets. Sci Data 12, 234 (2025). https://doi.org/10.1038/s41597-025-04558-z

## Acknowledgements

We would like to extend our thanks to all the authors involved in the 
development of this RD-CDM model.

---

- Authors:
  - [Adam SL Graefe](https://github.com/aslgraefe)
  - [Filip Rehburg](https://github.com/frehburg) 
  - [Samer Alkarkoukly](https://github.com/alkarkoukly)
  - [Daniel Danis](https://github.com/ielis)
  - [Peter N. Robinson](https://github.com/pnrobinson)
  - Oya Beyan
  - Sylvia Thun

