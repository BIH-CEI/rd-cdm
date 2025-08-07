# ontology-based rare disease common data model

Welcome to the repo of the ontology-based rare disease common data model 
(RD-CDM) harmonising international registry use, FHIR, and the Phenopacket 
Schema

<!-- Python CI and Documentation Status Badges -->
[![Python CI](https://github.com/BIH-CEI/rd-cdm/actions/workflows/python_ci.yml/badge.svg)](https://github.com/BIH-CEI/rd-cdm/actions/workflows/python_ci.yml)
[![Documentation Status](https://readthedocs.org/projects/rd-cdm/badge/?version=latest)](https://rd-cdm.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/863993011.svg)](https://doi.org/10.5281/zenodo.13891625)
![Python Versions](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue) 
[![LinkML](https://img.shields.io/badge/LinkML-1.8.0+-green.svg)](https://linkml.io/)

[Latest Documentation](https://rd-cdm.readthedocs.io/en/latest/)

### Manuscript

The corresponding paper of our RD-CDM v2.0.0 has now beed published at Nature
Scientific Data: https://www.nature.com/articles/s41597-025-04558-z

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Contributing & contact](#contributing-and-contact)
- [Resources](#resources-)
- [License](#license)
- [Citing](#citing)
- [Acknowledgements](#acknowledgements)

## Project Description

The ontology-based rare disease common data model (RD-CDM) is designed to 
harmonize rare disease data capture across international registries. It 
integrates standards such as the ERDRI-CDS, HL7 FHIR, and GA4GH Phenopacket 
Schema, creating a scalable, ontology-driven framework that supports advanced 
interoperability for research and care. The RD-CDM Version 2.0.0 consists of 
78 data elements, extending the ERDRI-CDS and allowing deeper insights into 
genetic findings, phenotypic features, and family history of individuals.

## Features

- Interoperability: Aligns with HL7 FHIR v4.0.1 and GA4GH Phenopacket v2.0 for
    structured data exchange.
- Ontology-driven: Utilizes ontologies such as SNOMED CT, LOINC, MONDO, OMIM, 
    and HPO for standardizing rare disease terminologies.
- Modular Structure: Comprises essential data elements categorized into formal 
    criteria, personal information, patient status, disease, genetic findings, 
    phenotypic findings, and family history.
- Cross-registry Compatibility: Enables data reuse across multiple registries 
    with consistent encoding and semantic alignment.

## Getting Started

This section provides instructions for getting started with the RD-CDM. For more
detail please read our [Documentation](https://rd-cdm.readthedocs.io/en/latest/)

### Prerequisites

- Python 3.x
- Dependencies in requirements.txt

### Installation

1. Clone the repository
  ```bash
  git clone https://github.com/BIH-CEI/rd-cdm.git
  cd rd-cdm
  ```

2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

3. Run tests to validate the JSON schema:
  ```bash
  pytest tests/
  ```

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

- [RareLink Docuemntation](https://rarelink.readthedocs.io/en/latest/index.html)
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
- Gene Ontology[🔗](https://geneontology.org/)
- NCI Thesaurus OBO Edition [🔗](https://obofoundry.org/ontology/ncit.html)

For the versions used in a specific RD-CDM version, please see the 
[resources in our documentation](https://rd-cdm.readthedocs.io/en/latest/resources/resources_file.html).

### Submodules
- [RareLink](https://github.com/BIH-CEI/RareLink)

## License

This project is licensed under the terms of the [MIT License](https://github.com/BIH-CEI/rd-cdm/blob/develop/LICENSE)

## Citing

If you use the model for your research, do not hesitate to reach out to and 
plase cite our article: 

> Graefe, A.S.L., Hübner, M.R., Rehburg, F. et al. An ontology-based rare disease common data model harmonising international registries, FHIR, and Phenopackets. Sci Data 12, 234 (2025). https://doi.org/10.1038/s41597-025-04558-z

## Acknowledgements

We would like to extend our thanks to all the authors involved in the 
development of this RD-CDM model. 

---

- Authors:
  - [Adam SL Graefe](https://github.com/aslgraefe)
  - [Filip Rehburg](https://github.com/frehburg) 
  - Miriam Hübner
  - Steffen Sander
  - Prof. Peter N. Robinson
  - Prof. Sylvia Thun
  - Prof. Oya Beyan
