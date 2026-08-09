---
search:
  boost: 5.0
---

# Slot: codes 


_List of allowed codes_



<div data-search-exclude markdown="1">



URI: [https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/codes](https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/codes)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ValueSet](ValueSet.md) | A set of permitted codes for a data element |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Coding](Coding.md) |
| Domain Of | [ValueSet](ValueSet.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ValueSet](ValueSet.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/codes |
| native | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/codes |




## LinkML Source

<details>
```yaml
name: codes
description: List of allowed codes
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml
rank: 1000
owner: ValueSet
domain_of:
- ValueSet
range: Coding
multivalued: true

```
</details></div>