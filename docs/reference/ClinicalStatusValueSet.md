---
search:
  boost: 2.0
---


# Enum: ClinicalStatusValueSet 




_Permitted codes for Clinical Status Value Set v2.0.0 (value set SNOMEDCT:263493007)._



<div data-search-exclude markdown="1">

URI: [rdcdm:ClinicalStatusValueSet](https://github.com/BIH-CEI/rd-cdm/ClinicalStatusValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| HL7FHIR:active | HL7FHIR:active | Active |
| HL7FHIR:recurrence | HL7FHIR:recurrence | Recurrence |
| HL7FHIR:relapse | HL7FHIR:relapse | Relapse |
| HL7FHIR:inactive | HL7FHIR:inactive | Inactive |
| HL7FHIR:remission | HL7FHIR:remission | Remission |
| HL7FHIR:resolved | HL7FHIR:resolved | Resolved |




## Slots

| Name | Description |
| ---  | --- |
| [5.8_Clinical_Status](5.8_Clinical_Status.md) | The clinical status of the disease indicates whetherit is active, inactive, o... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: ClinicalStatusValueSet
description: Permitted codes for Clinical Status Value Set v2.0.0 (value set SNOMEDCT:263493007).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  HL7FHIR:active:
    text: HL7FHIR:active
    description: Active
    meaning: HL7FHIR:active
  HL7FHIR:recurrence:
    text: HL7FHIR:recurrence
    description: Recurrence
    meaning: HL7FHIR:recurrence
  HL7FHIR:relapse:
    text: HL7FHIR:relapse
    description: Relapse
    meaning: HL7FHIR:relapse
  HL7FHIR:inactive:
    text: HL7FHIR:inactive
    description: Inactive
    meaning: HL7FHIR:inactive
  HL7FHIR:remission:
    text: HL7FHIR:remission
    description: Remission
    meaning: HL7FHIR:remission
  HL7FHIR:resolved:
    text: HL7FHIR:resolved
    description: Resolved
    meaning: HL7FHIR:resolved

```
</details>

</div>