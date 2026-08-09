---
search:
  boost: 2.0
---


# Enum: DeceasedValueSet 




_Permitted codes for Deceased Value Set v2.0.0 (value set SNOMEDCT:740604001)._



<div data-search-exclude markdown="1">

URI: [rdcdm:DeceasedValueSet](https://github.com/BIH-CEI/rd-cdm/DeceasedValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| SNOMEDCT:373066001 | SNOMEDCT:373066001 | True |
| SNOMEDCT:373067005 | SNOMEDCT:373067005 | False |
| SNOMEDCT:261665006 | SNOMEDCT:261665006 | Unknown |




## Slots

| Name | Description |
| ---  | --- |
| [6.4.10_Family_Member_Deceased](6.4.10_Family_Member_Deceased.md) | Indicates whether the selected family member is deceased |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: DeceasedValueSet
description: Permitted codes for Deceased Value Set v2.0.0 (value set SNOMEDCT:740604001).
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