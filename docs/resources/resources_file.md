# Resources

!!! tip
    The RD-CDM paper has been published in *Nature Scientific Data*.
    Read it [here](https://www.nature.com/articles/s41597-025-04558-z).

All resources below always reflect the **latest released version** of the
RD-CDM. The version is embedded in every file as `rd_cdm_version` and
`rd_cdm_date` — no need to check the filename.

To access a specific older version, install the corresponding PyPI release
(`pip install rd-cdm==2.0.2`) or browse the
[GitHub tags](https://github.com/BIH-CEI/rd-cdm/tags).

---

## Schema

The LinkML schema is the single source of truth for the data model structure
and version:

- [RD-CDM LinkML schema](../downloads/rd_cdm_schema.yaml)

`rd_cdm_profile.yaml` is generated from the instance data by `rd-cdm-profile`.
It expresses every value set as a bound LinkML enumeration and every data
element as a slot, so downstream models can import them rather than
re-declaring them. It is what the [Element Reference](../reference/index.md) is
rendered from:

- [RD-CDM element profile schema](../downloads/rd_cdm_profile.yaml)

See [LinkML](https://linkml.io/linkml/) for documentation on how to use them.

---

## Latest RD-CDM — Combined Files

The merged instance file contains all code systems, data elements, and value
sets in a single file, stamped with `rd_cdm_version` and `rd_cdm_date`:

- [RD-CDM merged YAML](../downloads/rd_cdm.yaml)
- [RD-CDM combined JSON](../downloads/rd_cdm.json)
- [RD-CDM combined CSV](../downloads/rd_cdm.csv)

Download all files as a ZIP archive from GitHub:

- [Download latest release as ZIP](https://github.com/BIH-CEI/rd-cdm/archive/refs/heads/main.zip)
- [Browse all tagged releases](https://github.com/BIH-CEI/rd-cdm/releases)

---

## Latest RD-CDM — Individual Components

### Code Systems

- [Code Systems YAML](../downloads/code_systems.yaml)
- [Code Systems JSON](../downloads/code_systems.json)
- [Code Systems CSV](../downloads/code_systems.csv)

### Data Elements

- [Data Elements YAML](../downloads/data_elements.yaml)
- [Data Elements JSON](../downloads/data_elements.json)
- [Data Elements CSV](../downloads/data_elements.csv)

### Value Sets

- [Value Sets YAML](../downloads/value_sets.yaml)
- [Value Sets JSON](../downloads/value_sets.json)
- [Value Sets CSV](../downloads/value_sets.csv)

---

## RD-CDM v2.0.0 (outdated)

The original v2.0.0 release is available on
[Figshare](https://figshare.com/articles/dataset/_b_Common_Data_Model_for_Rare_Diseases_b_based_on_the_ERDRI-CDS_HL7_FHIR_and_the_GA4GH_Phenopackets_Schema_v2_0_/26509150)
and as a
[GitHub release](https://github.com/BIH-CEI/rd-cdm/releases/tag/v2.0.0).

### Excel Table

- [RD-CDM v2.0.0 Excel Table](../_static/v2_0_0/RD-CDM%20v2.0.0.xlsx)

### JSON Files

- [Entire RD-CDM v2.0.0 JSON](../downloads/rd_cdm_v2_0_0.json)
- [Code Systems v2.0.0 JSON](../downloads/rd_cdm_codesystems_v2_0_0.json)
- [Data Elements v2.0.0 JSON](../downloads/rd_cdm_data_elements_v2_0_0.json)
- [Value Sets v2.0.0 JSON](../downloads/rd_cdm_value_sets_v2_0_0.json)

### CSV Files

- [Combined RD-CDM v2.0.0 CSV](../downloads/rd_cdm_v2_0_0.csv)
- [Code Systems v2.0.0 CSV](../downloads/rd_cdm_codesystems_v2_0_0.csv)
- [Data Elements v2.0.0 CSV](../downloads/rd_cdm_data_elements_v2_0_0.csv)
- [Value Sets v2.0.0 CSV](../downloads/rd_cdm_value_sets_v2_0_0.csv)

For additional details see [Background](../background/background_file.md).
