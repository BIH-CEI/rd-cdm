---
search:
  boost: 2.0
---


# Enum: UndiagnosedRDCaseValueSet 




_Permitted codes for Undiagnosed RD Case Value Set v2.0.0 (value set SNOMEDCT:723663001)._



<div data-search-exclude markdown="1">

URI: [rdcdm:UndiagnosedRDCaseValueSet](https://github.com/BIH-CEI/rd-cdm/UndiagnosedRDCaseValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| SNOMEDCT:373066001 | SNOMEDCT:373066001 | True |
| SNOMEDCT:373067005 | SNOMEDCT:373067005 | False |




## Slots

| Name | Description |
| ---  | --- |
| [3.6_Undiagnosed_RD_Case](3.6_Undiagnosed_RD_Case.md) | Identifies cases where an RD diagnosis has notbeen established |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: UndiagnosedRDCaseValueSet
description: Permitted codes for Undiagnosed RD Case Value Set v2.0.0 (value set SNOMEDCT:723663001).
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

```
</details>

</div>