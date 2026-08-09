---
search:
  boost: 5.0
---

# Slot: elementCodeSystem 


_Identifier of the code system (matches one of the `CodeSystem.id` values, e.g. “SNOMEDCT”, “LOINC”, “CustomCode”)._



<div data-search-exclude markdown="1">



URI: [https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/elementCodeSystem](https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/elementCodeSystem)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataElement](DataElement.md) | A single data field in the RD-CDM |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [DataElement](DataElement.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DataElement](DataElement.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/elementCodeSystem |
| native | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/elementCodeSystem |




## LinkML Source

<details>
```yaml
name: elementCodeSystem
description: Identifier of the code system (matches one of the `CodeSystem.id` values,
  e.g. “SNOMEDCT”, “LOINC”, “CustomCode”).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml
rank: 1000
owner: DataElement
domain_of:
- DataElement
range: string
required: true

```
</details></div>