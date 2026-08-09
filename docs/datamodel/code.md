---
search:
  boost: 5.0
---

# Slot: code 


_The code within the system_



<div data-search-exclude markdown="1">



URI: [https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/code](https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/code)
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
| Required | Yes |
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
| self | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/code |
| native | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/code |




## LinkML Source

<details>
```yaml
name: code
description: The code within the system
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml
rank: 1000
owner: Coding
domain_of:
- Coding
range: string
required: true

```
</details></div>