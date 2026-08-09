---
search:
  boost: 2.0
---


# Enum: InterpretationStatusValueSet 




_Permitted codes for Interpretation Status Value Set v2.0.0 (value set GA4GH:interpretation_status)._



<div data-search-exclude markdown="1">

URI: [rdcdm:InterpretationStatusValueSet](https://github.com/BIH-CEI/rd-cdm/InterpretationStatusValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| GA4GH:UNKNOWN_STATUS | GA4GH:UNKNOWN_STATUS | No information is available about the status |
| GA4GH:REJECTED | GA4GH:REJECTED | The variant or gene reported here is  interpreted not to be related to the di... |
| GA4GH:CANDIDATE | GA4GH:CANDIDATE | The variant or gene reported here is interpreted to possibly be related to th... |
| GA4GH:CONTRIBUTORY | GA4GH:CONTRIBUTORY | The variant or gene reported here is  interpreted to be related to the diagno... |
| GA4GH:CAUSATIVE | GA4GH:CAUSATIVE | The variant or gene reported here is  interpreted to be causative of the diag... |




## Slots

| Name | Description |
| ---  | --- |
| [6.1.3_Interpretation_Status](6.1.3_Interpretation_Status.md) | An enumeration that describes the conclusion made about the genomic interpret... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: InterpretationStatusValueSet
description: Permitted codes for Interpretation Status Value Set v2.0.0 (value set
  GA4GH:interpretation_status).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  GA4GH:UNKNOWN_STATUS:
    text: GA4GH:UNKNOWN_STATUS
    description: No information is available about the status
    meaning: GA4GH:UNKNOWN_STATUS
  GA4GH:REJECTED:
    text: GA4GH:REJECTED
    description: The variant or gene reported here is  interpreted not to be related
      to the diagnosis.
    meaning: GA4GH:REJECTED
  GA4GH:CANDIDATE:
    text: GA4GH:CANDIDATE
    description: The variant or gene reported here is interpreted to possibly be related
      to the diagnosis.
    meaning: GA4GH:CANDIDATE
  GA4GH:CONTRIBUTORY:
    text: GA4GH:CONTRIBUTORY
    description: The variant or gene reported here is  interpreted to be related to
      the diagnosis.
    meaning: GA4GH:CONTRIBUTORY
  GA4GH:CAUSATIVE:
    text: GA4GH:CAUSATIVE
    description: The variant or gene reported here is  interpreted to be causative
      of the diagnosis.
    meaning: GA4GH:CAUSATIVE

```
</details>

</div>