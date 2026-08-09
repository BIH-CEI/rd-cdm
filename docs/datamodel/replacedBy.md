---
search:
  boost: 5.0
---

# Slot: replacedBy 


_The CURIE of the active code that a value recorded under an inactive one migrates to. The successor must itself be a member of the same value set, so a legacy value can be migrated without leaving it. Absent where no equivalent has been agreed._

__



<div data-search-exclude markdown="1">



URI: [https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/replacedBy](https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/replacedBy)
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
| self | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/replacedBy |
| native | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/replacedBy |




## LinkML Source

<details>
```yaml
name: replacedBy
description: 'The CURIE of the active code that a value recorded under an inactive
  one migrates to. The successor must itself be a member of the same value set, so
  a legacy value can be migrated without leaving it. Absent where no equivalent has
  been agreed.

  '
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml
rank: 1000
owner: Coding
domain_of:
- Coding
range: string

```
</details></div>