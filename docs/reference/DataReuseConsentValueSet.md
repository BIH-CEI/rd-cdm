---
search:
  boost: 2.0
---


# Enum: DataReuseConsentValueSet 




_Permitted codes for Data Reuse Consent Value Set v2.0.0 (value set CustomCode:consent_data_reuse)._



<div data-search-exclude markdown="1">

URI: [rdcdm:DataReuseConsentValueSet](https://github.com/BIH-CEI/rd-cdm/DataReuseConsentValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| SNOMEDCT:373066001 | SNOMEDCT:373066001 | True |
| SNOMEDCT:373067005 | SNOMEDCT:373067005 | False |
| SNOMEDCT:261665006 | SNOMEDCT:261665006 | Unknown |




## Slots

| Name | Description |
| ---  | --- |
| [7.5_Consent_to_the_Reuse_of_Data](7.5_Consent_to_the_Reuse_of_Data.md) | Indicates whether the patient consents to the reuse of their data |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: DataReuseConsentValueSet
description: Permitted codes for Data Reuse Consent Value Set v2.0.0 (value set CustomCode:consent_data_reuse).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  SNOMEDCT:373066001:
    text: SNOMEDCT:373066001
    description: 'True'
    meaning: SNOMEDCT:373066001
  SNOMEDCT:373067005:
    text: SNOMEDCT:373067005
    description: 'False'
    meaning: SNOMEDCT:373067005
  SNOMEDCT:261665006:
    text: SNOMEDCT:261665006
    description: Unknown
    meaning: SNOMEDCT:261665006

```
</details>

</div>