---
search:
  boost: 2.0
---


# Enum: VitalStatusValueSet 




_Permitted codes for Vital Status Value Set v2.0.0 (value set SNOMEDCT:278844005)._



<div data-search-exclude markdown="1">

URI: [rdcdm:VitalStatusValueSet](https://github.com/BIH-CEI/rd-cdm/VitalStatusValueSet)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| SNOMEDCT:438949009 | SNOMEDCT:438949009 | Alive ||
| SNOMEDCT:419099009 | SNOMEDCT:419099009 | Dead ||
| SNOMEDCT:399307001 | SNOMEDCT:399307001 | Lost to follow-up | Title: Unknown - Lost in follow-up<br>|
| SNOMEDCT:185924006 | SNOMEDCT:185924006 | Unknown - Opted-out - INACTIVE, use SNOMEDCT:261665006 (Unknown) | Title: Unknown - Opted-out<br> **DEPRECATED**|
| SNOMEDCT:261665006 | SNOMEDCT:261665006 | Unknown | Title: Unknown - Other Reason<br>|




## Slots

| Name | Description |
| ---  | --- |
| [3.1_Vital_Status](3.1_Vital_Status.md) | The individual’s general clinical status orvital status |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: VitalStatusValueSet
description: Permitted codes for Vital Status Value Set v2.0.0 (value set SNOMEDCT:278844005).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  SNOMEDCT:438949009:
    text: SNOMEDCT:438949009
    description: Alive
    meaning: SNOMEDCT:438949009
  SNOMEDCT:419099009:
    text: SNOMEDCT:419099009
    description: Dead
    meaning: SNOMEDCT:419099009
  SNOMEDCT:399307001:
    text: SNOMEDCT:399307001
    description: Lost to follow-up
    meaning: SNOMEDCT:399307001
    title: Unknown - Lost in follow-up
  SNOMEDCT:185924006:
    text: SNOMEDCT:185924006
    description: Unknown - Opted-out - INACTIVE, use SNOMEDCT:261665006 (Unknown)
    meaning: SNOMEDCT:185924006
    title: Unknown - Opted-out
    deprecated: 'Does not resolve in BioPortal, which is this model''s terminology
      authority, so it is not offered for new capture. Retained, with replacedBy,
      so records already captured against it stay interpretable and can be migrated.
      Note that the successor is the generic Unknown: the opted-out *reason* is not
      preserved by the migration and belongs in the consent section rather than in
      vital status.'
  SNOMEDCT:261665006:
    text: SNOMEDCT:261665006
    description: Unknown
    meaning: SNOMEDCT:261665006
    title: Unknown - Other Reason

```
</details>

</div>