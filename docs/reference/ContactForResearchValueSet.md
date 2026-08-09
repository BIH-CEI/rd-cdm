---
search:
  boost: 2.0
---


# Enum: ContactForResearchValueSet 




_Permitted codes for Contact for Research Value Set v2.0.0 (value set CustomCode:consent_contact_research)._



<div data-search-exclude markdown="1">

URI: [rdcdm:ContactForResearchValueSet](https://github.com/BIH-CEI/rd-cdm/ContactForResearchValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| SNOMEDCT:373066001 | SNOMEDCT:373066001 | True |
| SNOMEDCT:373067005 | SNOMEDCT:373067005 | False |
| SNOMEDCT:261665006 | SNOMEDCT:261665006 | Unknown |




## Slots

| Name | Description |
| ---  | --- |
| [7.4_Agreement_to_be_Contacted_for_Research](7.4_Agreement_to_be_Contacted_for_Research.md) | Indicates whether the patient agrees to be contacted for research |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: ContactForResearchValueSet
description: Permitted codes for Contact for Research Value Set v2.0.0 (value set
  CustomCode:consent_contact_research).
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