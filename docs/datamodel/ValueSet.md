---
search:
  boost: 5.0
---

# Slot: valueSet 


_The `label` of the ValueSet constraining this element - not its `id`. Value set labels are therefore unique, and a value set's `id` is by convention the CURIE of the element it constrains. Both are enforced by `rd_cdm.utils.structure_checks`._

__



<div data-search-exclude markdown="1">



URI: [https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/valueSet](https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/valueSet)
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
| self | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/valueSet |
| native | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/valueSet |




## LinkML Source

<details>
```yaml
name: valueSet
description: 'The `label` of the ValueSet constraining this element - not its `id`.
  Value set labels are therefore unique, and a value set''s `id` is by convention
  the CURIE of the element it constrains. Both are enforced by `rd_cdm.utils.structure_checks`.

  '
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml
rank: 1000
owner: DataElement
domain_of:
- DataElement
range: string

```
</details></div>