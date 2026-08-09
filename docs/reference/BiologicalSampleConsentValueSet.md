---
search:
  boost: 2.0
---


# Enum: BiologicalSampleConsentValueSet 




_Permitted codes for Biological Sample Consent Value Set v2.0.0 (value set SNOMEDCT:123038009)._



<div data-search-exclude markdown="1">

URI: [rdcdm:BiologicalSampleConsentValueSet](https://github.com/BIH-CEI/rd-cdm/BiologicalSampleConsentValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| SNOMEDCT:373066001 | SNOMEDCT:373066001 | True |
| SNOMEDCT:373067005 | SNOMEDCT:373067005 | False |
| SNOMEDCT:261665006 | SNOMEDCT:261665006 | Unknown |




## Slots

| Name | Description |
| ---  | --- |
| [7.6_Biological_Sample](7.6_Biological_Sample.md) | Indicates whether a patient's biological sample is available for research |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: BiologicalSampleConsentValueSet
description: Permitted codes for Biological Sample Consent Value Set v2.0.0 (value
  set SNOMEDCT:123038009).
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