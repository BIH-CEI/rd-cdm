---
search:
  boost: 5.0
---

# Slot: elementCode 


_Primary code describing the element_



<div data-search-exclude markdown="1">



URI: [https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/elementCode](https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/elementCode)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataElement](DataElement.md) | A single data field in the RD-CDM |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Coding](Coding.md) |
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
| self | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/elementCode |
| native | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/elementCode |




## LinkML Source

<details>
```yaml
name: elementCode
description: Primary code describing the element
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml
rank: 1000
owner: DataElement
domain_of:
- DataElement
range: Coding
required: true

```
</details></div>