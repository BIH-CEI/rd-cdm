---
search:
  boost: 2.0
---


# Enum: ClinicalSignificanceACMGValueSet 




_Permitted codes for Clinical Significance ACMG Value Set v2.0.0 (value set LOINC:53037-8)._



<div data-search-exclude markdown="1">

URI: [rdcdm:ClinicalSignificanceACMGValueSet](https://github.com/BIH-CEI/rd-cdm/ClinicalSignificanceACMGValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| LOINC:LA6668-3 | LOINC:LA6668-3 | Pathogenic |
| LOINC:LA26332-9 | LOINC:LA26332-9 | Likely pathogenic |
| LOINC:LA26333-7 | LOINC:LA26333-7 | Uncertain significance |
| LOINC:LA26334-5 | LOINC:LA26334-5 | Likely benign |
| LOINC:LA6675-8 | LOINC:LA6675-8 | Benign |
| LOINC:LA4489-6 | LOINC:LA4489-6 | Unknown |




## Slots

| Name | Description |
| ---  | --- |
| [6.1.14_Clinical_Significance_ACMG](6.1.14_Clinical_Significance_ACMG.md) | The clinical significance of the genetic variant, indicating its impact on he... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: ClinicalSignificanceACMGValueSet
description: Permitted codes for Clinical Significance ACMG Value Set v2.0.0 (value
  set LOINC:53037-8).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  LOINC:LA6668-3:
    text: LOINC:LA6668-3
    description: Pathogenic
    meaning: LOINC:LA6668-3
  LOINC:LA26332-9:
    text: LOINC:LA26332-9
    description: Likely pathogenic
    meaning: LOINC:LA26332-9
  LOINC:LA26333-7:
    text: LOINC:LA26333-7
    description: Uncertain significance
    meaning: LOINC:LA26333-7
  LOINC:LA26334-5:
    text: LOINC:LA26334-5
    description: Likely benign
    meaning: LOINC:LA26334-5
  LOINC:LA6675-8:
    text: LOINC:LA6675-8
    description: Benign
    meaning: LOINC:LA6675-8
  LOINC:LA4489-6:
    text: LOINC:LA4489-6
    description: Unknown
    meaning: LOINC:LA4489-6

```
</details>

</div>