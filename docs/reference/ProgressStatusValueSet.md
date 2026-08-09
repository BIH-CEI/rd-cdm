---
search:
  boost: 2.0
---


# Enum: ProgressStatusValueSet 




_Permitted codes for Progress Status Value Set v2.0.0 (value set GA4GH:progress_status)._



<div data-search-exclude markdown="1">

URI: [rdcdm:ProgressStatusValueSet](https://github.com/BIH-CEI/rd-cdm/ProgressStatusValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| GA4GH:UNKNOWN_PROGRESS | GA4GH:UNKNOWN_PROGRESS | No information is available aboutthe diagnosis |
| GA4GH:IN_PROGRESS | GA4GH:IN_PROGRESS | No diagnosis has been found to date but additional differential diagnostic wo... |
| GA4GH:COMPLETED | GA4GH:COMPLETED | The work on the interpretation is complete |
| GA4GH:SOLVED | GA4GH:SOLVED | The interpretation is complete and also considered to be a definitive diagnos... |
| GA4GH:UNSOLVED | GA4GH:UNSOLVED | The interpretation is complete but no definitive diagnosiswas found |




## Slots

| Name | Description |
| ---  | --- |
| [6.1.2_Progress_Status_of_Interpretation](6.1.2_Progress_Status_of_Interpretation.md) | The interpretation has a ProgressStatus that refers tothe status of the attem... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: ProgressStatusValueSet
description: Permitted codes for Progress Status Value Set v2.0.0 (value set GA4GH:progress_status).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  GA4GH:UNKNOWN_PROGRESS:
    text: GA4GH:UNKNOWN_PROGRESS
    description: No information is available aboutthe diagnosis
    meaning: GA4GH:UNKNOWN_PROGRESS
  GA4GH:IN_PROGRESS:
    text: GA4GH:IN_PROGRESS
    description: No diagnosis has been found to date but additional differential diagnostic
      work is in progress.
    meaning: GA4GH:IN_PROGRESS
  GA4GH:COMPLETED:
    text: GA4GH:COMPLETED
    description: The work on the interpretation is complete.
    meaning: GA4GH:COMPLETED
  GA4GH:SOLVED:
    text: GA4GH:SOLVED
    description: The interpretation is complete and also considered to be a definitive
      diagnosis.
    meaning: GA4GH:SOLVED
  GA4GH:UNSOLVED:
    text: GA4GH:UNSOLVED
    description: The interpretation is complete but no definitive diagnosiswas found.
    meaning: GA4GH:UNSOLVED

```
</details>

</div>