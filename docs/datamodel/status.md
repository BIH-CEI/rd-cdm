---
search:
  boost: 5.0
---

# Slot: status 


_Lifecycle of this code against the model's terminology authority. Defaults to `active`. `inactive` records that the code no longer resolves in BioPortal, which is the single authority this model validates against - the RD-CDM does not consult a terminology's own release files, so this is a statement about resolvability, not a claim about why the concept was withdrawn._

_An inactive code MUST NOT be offered for new data capture: a generator building a form or dropdown from this value set filters to `active`. It is kept in the value set so that data already captured against it stays interpretable - terminologies do not reuse identifiers, so the code still means exactly what it meant when it was recorded._

__



<div data-search-exclude markdown="1">



URI: [https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/status](https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Coding](Coding.md) | A code + code system reference |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CodeStatus](CodeStatus.md) |
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
| self | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/status |
| native | https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/status |




## LinkML Source

<details>
```yaml
name: status
description: 'Lifecycle of this code against the model''s terminology authority. Defaults
  to `active`. `inactive` records that the code no longer resolves in BioPortal, which
  is the single authority this model validates against - the RD-CDM does not consult
  a terminology''s own release files, so this is a statement about resolvability,
  not a claim about why the concept was withdrawn.

  An inactive code MUST NOT be offered for new data capture: a generator building
  a form or dropdown from this value set filters to `active`. It is kept in the value
  set so that data already captured against it stays interpretable - terminologies
  do not reuse identifiers, so the code still means exactly what it meant when it
  was recorded.

  '
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml
rank: 1000
owner: Coding
domain_of:
- Coding
range: CodeStatus

```
</details></div>