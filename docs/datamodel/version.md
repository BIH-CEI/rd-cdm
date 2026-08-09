---
search:
  boost: 5.0
---

# Slot: version 


_The release version or publication date of the ontology_



<div data-search-exclude markdown="1">



URI: [https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/version](https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/version)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CodeSystem](CodeSystem.md) | Metadata for an ontology or code system |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
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
| self | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/version |
| native | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/version |




## LinkML Source

<details>
```yaml
name: version
description: The release version or publication date of the ontology
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml
rank: 1000
owner: CodeSystem
domain_of:
- CodeSystem
range: string
required: true

```
</details></div>