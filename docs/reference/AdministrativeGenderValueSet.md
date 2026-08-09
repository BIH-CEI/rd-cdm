---
search:
  boost: 2.0
---


# Enum: AdministrativeGenderValueSet 




_Permitted codes for AdministrativeGender Value Set v2.0.0 (value set LOINC:54123-5)._



<div data-search-exclude markdown="1">

URI: [rdcdm:AdministrativeGenderValueSet](https://github.com/BIH-CEI/rd-cdm/AdministrativeGenderValueSet)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| SNOMEDCT:248152002 | SNOMEDCT:248152002 | Female ||
| SNOMEDCT:248153007 | SNOMEDCT:248153007 | Male ||
| SNOMEDCT:184115007 | SNOMEDCT:184115007 | Patient sex unknown - INACTIVE, use SNOMEDCT:261665006 (Unknown) | **DEPRECATED**|
| SNOMEDCT:32570691000036108 | SNOMEDCT:32570691000036108 | Intersex ||
| SNOMEDCT:261665006 | SNOMEDCT:261665006 | Unknown ||
| SNOMEDCT:1220561009 | SNOMEDCT:1220561009 | Not recorded ||




## Slots

| Name | Description |
| ---  | --- |
| [6.4.7_Family_Member_Sex](6.4.7_Family_Member_Sex.md) | Specifies the sex (or gender) of the specific family member |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: AdministrativeGenderValueSet
description: Permitted codes for AdministrativeGender Value Set v2.0.0 (value set
  LOINC:54123-5).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  SNOMEDCT:248152002:
    text: SNOMEDCT:248152002
    description: Female
    meaning: SNOMEDCT:248152002
  SNOMEDCT:248153007:
    text: SNOMEDCT:248153007
    description: Male
    meaning: SNOMEDCT:248153007
  SNOMEDCT:184115007:
    text: SNOMEDCT:184115007
    description: Patient sex unknown - INACTIVE, use SNOMEDCT:261665006 (Unknown)
    meaning: SNOMEDCT:184115007
    deprecated: 'Does not resolve in BioPortal, which is this model''s terminology
      authority, so it is not offered for new capture. Retained, with replacedBy,
      so records already captured against it stay interpretable and can be migrated:
      identifiers are never reused, so the code still means what it meant when it
      was recorded.'
  SNOMEDCT:32570691000036108:
    text: SNOMEDCT:32570691000036108
    description: Intersex
    meaning: SNOMEDCT:32570691000036108
  SNOMEDCT:261665006:
    text: SNOMEDCT:261665006
    description: Unknown
    meaning: SNOMEDCT:261665006
  SNOMEDCT:1220561009:
    text: SNOMEDCT:1220561009
    description: Not recorded
    meaning: SNOMEDCT:1220561009

```
</details>

</div>