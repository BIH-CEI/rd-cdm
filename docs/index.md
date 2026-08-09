# Welcome to the RD-CDM Documentation

[![Documentation Status](https://readthedocs.org/projects/rd-cdm/badge/?version=latest)](https://rd-cdm.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/rd-cdm.svg)](https://pypi.org/project/rd-cdm/)

The ontology-based rare disease common data model (RD-CDM) is a non-balloted
extension of the ERDRI-CDS which aims to provide an internationally viable
template for the development and implementation of country-specific rare disease
common data models. The RD-CDM is designed to be compatible with the GA4GH
Phenopacket Schema, HL7 FHIR, and the International Patient Summary. The
ontology-based approach of the RD-CDM allows for the integration of various data
sources and the harmonization of data across different systems.

!!! tip
    The RD-CDM paper has now been published at Nature Scientific Data. You can
    read it [here](https://www.nature.com/articles/s41597-025-04558-z)!

## Where to start

<div class="grid cards" markdown>

- **[Background](background/background_file.md)** — what the RD-CDM is, how it
  was developed, and the layers of harmonisation it defines.

- **[Element Reference](reference/index.md)** — every data element and value
  set, with its ontology codes, FHIR expression and Phenopacket mapping.

- **[Resources](resources/resources_file.md)** — download the schema, the
  instances, and the JSON and CSV exports.

- **[Usage](usage/usage_file.md)** — using the RD-CDM, and RareLink.

</div>

## Install

```bash
pip install rd-cdm
```

The `version` in the LinkML schema is the single source of truth for the model
version, and every exported YAML, JSON and CSV file carries `rd_cdm_version` and
`rd_cdm_date` so outputs are unambiguous.

## Citing

> Graefe, A.S.L., Hübner, M.R., Rehburg, F. et al. An ontology-based rare
> disease common data model harmonising international registries, FHIR, and
> Phenopackets. *Sci Data* 12, 234 (2025).
> <https://doi.org/10.1038/s41597-025-04558-z>
