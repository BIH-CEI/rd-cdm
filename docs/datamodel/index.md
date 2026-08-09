# Data Model Reference

Generated from `schema/rd_cdm.yaml` (RD-CDM 2.1.0) with LinkML `gen-doc`.
Do not edit these files by hand — run `rd-cdm-docs` after changing the schema.

This documents the *container*: the classes an RD-CDM document is built from.
For the data elements and value sets themselves, see the
[Element Reference](../reference/index.md).

# ontology-based rare disease common data model (RD-CDM) harmonising international registries, FHIR, and Phenopackets



URI: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml

Name: rd-cdm



## Classes

| Class | Description |
| --- | --- |
| [CodeSystem](CodeSystem.md) | Metadata for an ontology or code system |
| [Coding](Coding.md) | A code + code system reference |
| [DataElement](DataElement.md) | A single data field in the RD-CDM |
| [RdCdm](RdCdm.md) | Root class for the Rare Disease Common Data Model (RD-CDM) |
| [ValueSet](ValueSet.md) | A set of permitted codes for a data element |



## Slots

| Slot | Description |
| --- | --- |
| [code](code.md) | The code within the system |
| [code_systems](code_systems.md) |  |
| [codes](codes.md) | List of allowed codes |
| [data_elements](data_elements.md) |  |
| [dataSpecification](dataSpecification.md) | Reference or link to specification |
| [dataType](dataType.md) | Data type (e |
| [description](description.md) | Full textual description of the element |
| [displayLabel](displayLabel.md) | An optional presentation label for user interfaces and data capture forms, us... |
| [elementCode](elementCode.md) | Primary code describing the element |
| [elementCodeSystem](elementCodeSystem.md) | Identifier of the code system (matches one of the `CodeSystem |
| [elementName](elementName.md) | Human-readable name of the element |
| [fhirExpression_v4_0_1](fhirExpression_v4_0_1.md) | FHIRPath expression for FHIR mapping |
| [homepage](homepage.md) | A URL for human browsing or documentation |
| [id](id.md) | The CURIE prefix used for terms in this code system (e |
| [label](label.md) | The preferred label of the code in its source terminology |
| [namespace_iri](namespace_iri.md) | The base namespace IRI for this ontology, used by OAKlib to expand CURIEs and... |
| [ordinal](ordinal.md) | Position within the form or section |
| [phenopacketSchemaElement_v2_0](phenopacketSchemaElement_v2_0.md) | Phenopacket schema path |
| [rd_cdm_date](rd_cdm_date.md) | Date of the RD-CDM release |
| [rd_cdm_version](rd_cdm_version.md) | Version of the RD-CDM schema |
| [recommendedDataSpec_fhir](recommendedDataSpec_fhir.md) | Recommendations for FHIR profiling |
| [recommendedDataSpec_phenopackets](recommendedDataSpec_phenopackets.md) | Recommended Phenopacket datatype or format |
| [replacedBy](replacedBy.md) | The CURIE of the active code that a value recorded under an inactive one migr... |
| [section](section.md) | Logical grouping or heading |
| [status](status.md) | Lifecycle of this code against the model's terminology authority |
| [statusNote](statusNote.md) | Why a code carries a non-default status, and what a consumer should do about ... |
| [system](system.md) | CURIE for the code system |
| [title](title.md) | A human-readable title for this code system |
| [value_sets](value_sets.md) |  |
| [valueSet](valueSet.md) | The `label` of the ValueSet constraining this element - not its `id` |
| [version](version.md) | The release version or publication date of the ontology |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [CodeStatus](CodeStatus.md) | Whether a code still resolves against BioPortal, the single terminology autho... |


## Types

| Type | Description |
| --- | --- |


## Subsets

| Subset | Description |
| --- | --- |
