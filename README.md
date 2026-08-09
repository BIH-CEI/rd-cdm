# ontology-based rare disease common data model

Welcome to the repo of the ontology-based rare disease common data model (RD-CDM)
harmonising international registry use, HL7® FHIR®, and the GA4GH Phenopacket Schema.

[![CI](https://github.com/BIH-CEI/rd-cdm/actions/workflows/ci.yml/badge.svg)](https://github.com/BIH-CEI/rd-cdm/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/rd-cdm/badge/?version=latest)](https://rd-cdm.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/863993011.svg)](https://doi.org/10.5281/zenodo.13891625)
![Python Versions](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12-blue)
[![PyPI](https://img.shields.io/pypi/v/rd-cdm.svg)](https://pypi.org/project/rd-cdm/)
[![Downloads](https://img.shields.io/pypi/dm/rd-cdm.svg?label=downloads)](https://pypi.org/project/rd-cdm/)
[![LinkML](https://img.shields.io/badge/LinkML-1.9.0+-green.svg)](https://linkml.io/)

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
- [Validating with BioPortal](#validating-with-bioportal)
- [Contributing & Contact](#contributing--contact)
- [Resources](#resources)
- [License](#license)
- [Citing](#citing)
- [Acknowledgements](#acknowledgements)

---

## Project Description

The ontology-based RD-CDM harmonizes rare disease data capture across registries.
It integrates ERDRI-CDS, HL7 FHIR, and GA4GH Phenopacket Schema to support
interoperable data for research and care. RD-CDM v2.0.x comprises 78 data elements
covering formal criteria, personal information, patient status, disease, genetic
findings, phenotypic findings, and family history.

---

## What you get from PyPI

Installing `rd-cdm` from PyPI provides:

- **Schema**
  - `src/rd_cdm/schema/rd_cdm.yaml` — LinkML schema defining the data model
    structure. The `version` and `date` fields here are the single source of
    truth for the data model version.

- **Instances**
  - `src/rd_cdm/instances/code_systems.yaml`
  - `src/rd_cdm/instances/data_elements.yaml`
  - `src/rd_cdm/instances/value_sets.yaml`
  - `src/rd_cdm/instances/rd_cdm.yaml` — merged instance, version-stamped
    with `rd_cdm_version` and `rd_cdm_date` at the top
  - `src/rd_cdm/instances/jsons/rd_cdm.json`
  - `src/rd_cdm/instances/csvs/rd_cdm.csv`

- **Generated Python classes (LinkML)**
  - `src/rd_cdm/python_classes/rd_cdm.py` — LinkML runtime dataclasses
  - `src/rd_cdm/python_classes/rd_cdm_pydantic.py` — Pydantic v2 models

- **CLI entry points**
  - `rd-cdm-merge` — merge instance parts into `rd_cdm.yaml`
  - `rd-cdm-json` — export to `jsons/rd_cdm.json`
  - `rd-cdm-csv` — export to `csvs/rd_cdm.csv`
  - `rd-cdm-validate` — validate ontology codes via BioPortal

---

## Features

- **Interoperability**: Aligns with HL7 FHIR v4.0.1 and GA4GH Phenopacket v2.0
- **Ontology-driven**: Uses SNOMED CT, LOINC, NCIT, MONDO, OMIM, HPO, and more
- **Modular**: Clear separation of schema, instances, and exports
- **Self-describing exports**: Every YAML, JSON, and CSV file carries
  `rd_cdm_version` and `rd_cdm_date` so outputs are unambiguous without
  needing to know which package version was installed
- **Tooling**: Merge, export, and validation utilities via simple CLI commands
- **Pydantic models**: Runtime validation generated from the LinkML schema

---

## Installation

From PyPI:
```bash
pip install rd-cdm
```

Optional extras:
```bash
pip install rd-cdm[test]   # pytest, requests-mock
pip install rd-cdm[docs]   # mkdocs and the material theme
pip install rd-cdm[dev]    # linkml (for regenerating Python classes and docs)
```

### Development install
```bash
git clone https://github.com/BIH-CEI/rd-cdm.git
cd rd-cdm
python -m venv .venv && source .venv/bin/activate
pip install -U pip
pip install -e ".[test,dev]"
pytest -q
```

> We use a **src/** layout. Use the installed CLI entry points shown below
> rather than running scripts directly.

---

## CLI tools

After installation the following commands are available:
```bash
# Merge instance parts → src/rd_cdm/instances/rd_cdm.yaml
rd-cdm-merge

# Export merged YAML → src/rd_cdm/instances/jsons/rd_cdm.json
rd-cdm-json

# Export merged YAML → src/rd_cdm/instances/csvs/rd_cdm.csv
rd-cdm-csv

# Validate all ontology codes against BioPortal
rd-cdm-validate
```

The recommended order when updating the model is:
```bash
rd-cdm-merge && rd-cdm-json && rd-cdm-csv && rd-cdm-validate
```

---

## Validating with BioPortal

`rd-cdm-validate` checks all ontology codes in the merged instance against
BioPortal and reports version drift and missing or deprecated terms.

### Get an API key

Sign up at https://bioportal.bioontology.org/accounts/new, go to your account
settings, and copy your API key.

### Set the environment variable

macOS / Linux:
```bash
export BIOPORTAL_API_KEY="your-key-here"
```

Windows (PowerShell):
```powershell
setx BIOPORTAL_API_KEY "your-key-here"
```

---

## Contributing and Contact

The RD-CDM is a community-driven effort. Please feel free to open issues,
discuss features, or submit pull requests. For larger contributions consider
reaching out directly.

See the [`Contributing` section of our documentation](https://rd-cdm.readthedocs.io/en/latest/contributing.html)
for full guidelines.

## RareLink

RareLink is a REDCap-based framework for rare disease research linking
international registries to FHIR and Phenopackets, built on the RD-CDM.

- [RareLink Documentation](https://rarelink.readthedocs.io/en/latest/index.html)
- [RareLink GitHub](https://github.com/BIH-CEI/rarelink)

---

## Resources

### Ontologies

- Human Phenotype Ontology [🔗](http://www.human-phenotype-ontology.org)
- Monarch Initiative Disease Ontology [🔗](https://mondo.monarchinitiative.org/)
- Online Mendelian Inheritance in Man [🔗](https://www.omim.org/)
- Orphanet Rare Disease Ontology [🔗](https://www.orpha.net/)
- SNOMED CT [🔗](https://www.snomed.org/snomed-ct)
- ICD-11 [🔗](https://icd.who.int/en)
- ICD-10-CM [🔗](https://www.cdc.gov/nchs/icd/icd10cm.htm)
- NCBI Taxonomy [🔗](https://www.ncbi.nlm.nih.gov/taxonomy)
- LOINC [🔗](https://loinc.org/)
- HGNC [🔗](https://www.genenames.org/)
- NCI Thesaurus OBO Edition [🔗](https://obofoundry.org/ontology/ncit.html)

For the ontology versions used in each RD-CDM release, see the
[resources page in our documentation](https://rd-cdm.readthedocs.io/en/latest/resources/resources_file.html).

---

## License

[MIT License](https://github.com/BIH-CEI/rd-cdm/blob/main/LICENSE)

## Citing

> Graefe, A.S.L., Hübner, M.R., Rehburg, F. et al. An ontology-based rare
> disease common data model harmonising international registries, FHIR, and
> Phenopackets. *Sci Data* 12, 234 (2025).
> https://doi.org/10.1038/s41597-025-04558-z

## Acknowledgements

- [Adam SL Graefe](https://github.com/aslgraefe)
- [Filip Rehburg](https://github.com/frehburg)
- [Samer Alkarkoukly](https://github.com/alkarkoukly)
- [Daniel Danis](https://github.com/ielis)
- [Peter N. Robinson](https://github.com/pnrobinson)
- Oya Beyan
- Sylvia Thun