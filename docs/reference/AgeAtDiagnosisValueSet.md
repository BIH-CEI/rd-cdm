---
search:
  boost: 2.0
---


# Enum: AgeAtDiagnosisValueSet 




_Permitted codes for Age at Diagnosis Value Set v2.0.0 (value set SNOMEDCT:423493009)._



<div data-search-exclude markdown="1">

URI: [rdcdm:AgeAtDiagnosisValueSet](https://github.com/BIH-CEI/rd-cdm/AgeAtDiagnosisValueSet)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| SNOMEDCT:118189007 | SNOMEDCT:118189007 | Prenatal finding | Title: Prenatal<br>|
| SNOMEDCT:3950001 | SNOMEDCT:3950001 | Birth ||
| SNOMEDCT:410672004 | SNOMEDCT:410672004 | Date ||
| SNOMEDCT:261665006 | SNOMEDCT:261665006 | Unknown ||




## Slots

| Name | Description |
| ---  | --- |
| [5.5_Age_at_Diagnosis](5.5_Age_at_Diagnosis.md) | The individual’s age when the diagnosis was made |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: AgeAtDiagnosisValueSet
description: Permitted codes for Age at Diagnosis Value Set v2.0.0 (value set SNOMEDCT:423493009).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  SNOMEDCT:118189007:
    text: SNOMEDCT:118189007
    description: Prenatal finding
    meaning: SNOMEDCT:118189007
    title: Prenatal
  SNOMEDCT:3950001:
    text: SNOMEDCT:3950001
    description: Birth
    meaning: SNOMEDCT:3950001
  SNOMEDCT:410672004:
    text: SNOMEDCT:410672004
    description: Date
    meaning: SNOMEDCT:410672004
  SNOMEDCT:261665006:
    text: SNOMEDCT:261665006
    description: Unknown
    meaning: SNOMEDCT:261665006

```
</details>

</div>