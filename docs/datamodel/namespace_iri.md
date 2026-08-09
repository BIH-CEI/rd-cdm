---
search:
  boost: 5.0
---

# Slot: namespace_iri 


_The base namespace IRI for this ontology, used by OAKlib to expand CURIEs and load the adapter._

__



<div data-search-exclude markdown="1">



URI: [https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/namespace_iri](https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/namespace_iri)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CodeSystem](CodeSystem.md) | Metadata for an ontology or code system |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [CodeSystem](CodeSystem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CodeSystem](CodeSystem.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/namespace_iri |
| native | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/namespace_iri |




## LinkML Source

<details>
```yaml
name: namespace_iri
description: 'The base namespace IRI for this ontology, used by OAKlib to expand CURIEs
  and load the adapter.

  '
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml
rank: 1000
owner: CodeSystem
domain_of:
- CodeSystem
range: uri
required: true

```
</details></div>