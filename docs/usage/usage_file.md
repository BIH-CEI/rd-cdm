# Usage

!!! tip
    The RD-CDM paper has now been published at Nature Scientific Data. You can
    read it [here](https://www.nature.com/articles/s41597-025-04558-z)!

The RD-CDM is developed within an open-source community and is available for use
by researchers, clinicians, and other stakeholders in the rare disease community.
The RD-CDM is designed to support the collection of harmonized data for rare
disease research and treatment, making interoperability a crucial enabler for
improving outcomes in RD care.

Please see the [License](../license.md) for information on the RD-CDM license.

!!! note
    The RD-CDM is a community-driven project, and we welcome contributions from
    researchers, clinicians, and other stakeholders in the rare disease
    community. If you would like to contribute to the RD-CDM, please read our
    [Contributing](../contributing.md) guidelines.

## Install

```bash
pip install rd-cdm
```

Optional extras:

```bash
pip install rd-cdm[test]   # pytest, requests-mock
pip install rd-cdm[docs]   # mkdocs and the material theme
pip install rd-cdm[dev]    # linkml, for regenerating classes and documentation
```

## CLI tools

| Command | Does |
|---|---|
| `rd-cdm-merge` | merges the instance parts into `instances/rd_cdm.yaml` |
| `rd-cdm-json` | exports to `instances/jsons/` |
| `rd-cdm-csv` | exports to `instances/csvs/` |
| `rd-cdm-profile` | projects the instances into `schema/rd_cdm_profile.yaml` |
| `rd-cdm-validate` | validates every ontology code against BioPortal |
| `rd-cdm-sync-versions` | applies code system version drift from BioPortal |
| `rd-cdm-docs` | regenerates the element and data model references |

The recommended order after changing the instance files:

```bash
rd-cdm-merge && rd-cdm-profile && rd-cdm-json && rd-cdm-csv && rd-cdm-validate
```

`rd-cdm-validate --offline` runs the structural checks only. It needs no
BioPortal key and takes seconds rather than minutes, so it is the right one to
run while editing.

## Validating with BioPortal

`rd-cdm-validate` checks all ontology codes in the merged instance against
BioPortal and reports version drift, label drift and unresolvable codes.

Sign up at <https://bioportal.bioontology.org/accounts/new>, go to your account
settings, and copy your API key.

=== "macOS / Linux"

    ```bash
    export BIOPORTAL_API_KEY="your-key-here"
    ```

=== "Windows (PowerShell)"

    ```powershell
    setx BIOPORTAL_API_KEY "your-key-here"
    ```

## RareLink

RareLink is a novel rare disease framework in REDCap linking international
registries, FHIR, and Phenopackets based on the RD-CDM. It is designed to
support the collection of harmonized data for rare disease research across any
REDCap project worldwide and allows for the preconfigured export of the RD-CDM
data in FHIR and Phenopackets formats.

For more information on RareLink, please see:

- RareLink paper published in npj Genomic Medicine (2025):
  <https://www.nature.com/articles/s41525-025-00534-z>
- RareLink Documentation: <https://rarelink.readthedocs.io/en/latest/index.html>
- RareLink GitHub: <https://github.com/BIH-CEI/rarelink>
