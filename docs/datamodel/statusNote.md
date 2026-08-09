---
search:
  boost: 5.0
---

# Slot: statusNote 


_Why a code carries a non-default status, and what a consumer should do about it. Required in practice for inactive codes._

__



<div data-search-exclude markdown="1">



URI: [https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/statusNote](https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/statusNote)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Coding](Coding.md) | A code + code system reference |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:string](http://www.w3.org/2001/XMLSchema#string) |
| Domain Of | [Coding](Coding.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Coding](Coding.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/statusNote |
| native | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/statusNote |




## LinkML Source

<details>
```yaml
name: statusNote
description: 'Why a code carries a non-default status, and what a consumer should
  do about it. Required in practice for inactive codes.

  '
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml
rank: 1000
owner: Coding
domain_of:
- Coding
range: string

```
</details></div>