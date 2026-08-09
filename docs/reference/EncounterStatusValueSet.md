---
search:
  boost: 2.0
---


# Enum: EncounterStatusValueSet 




_Permitted codes for Encounter Status Value Set v2.0.0 (value set SNOMEDCT:305058001)._



<div data-search-exclude markdown="1">

URI: [rdcdm:EncounterStatusValueSet](https://github.com/BIH-CEI/rd-cdm/EncounterStatusValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| HL7FHIR:planned | HL7FHIR:planned | Planned |
| HL7FHIR:arrived | HL7FHIR:arrived | Arrived |
| HL7FHIR:triaged | HL7FHIR:triaged | Triaged |
| HL7FHIR:in-progress | HL7FHIR:in-progress | In Progress |
| HL7FHIR:onleave | HL7FHIR:onleave | On Leave |
| HL7FHIR:finished | HL7FHIR:finished | Finished |
| HL7FHIR:cancelled | HL7FHIR:cancelled | Cancelled |
| HL7FHIR:entered-in-error | HL7FHIR:entered-in-error | Entered in Error |
| HL7FHIR:unknown | HL7FHIR:unknown | Unknown |




## Slots

| Name | Description |
| ---  | --- |
| [4.3_Encounter_Status](4.3_Encounter_Status.md) | The status of an encounter of the individual at thetime of data capture |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: EncounterStatusValueSet
description: Permitted codes for Encounter Status Value Set v2.0.0 (value set SNOMEDCT:305058001).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  HL7FHIR:planned:
    text: HL7FHIR:planned
    description: Planned
    meaning: HL7FHIR:planned
  HL7FHIR:arrived:
    text: HL7FHIR:arrived
    description: Arrived
    meaning: HL7FHIR:arrived
  HL7FHIR:triaged:
    text: HL7FHIR:triaged
    description: Triaged
    meaning: HL7FHIR:triaged
  HL7FHIR:in-progress:
    text: HL7FHIR:in-progress
    description: In Progress
    meaning: HL7FHIR:in-progress
  HL7FHIR:onleave:
    text: HL7FHIR:onleave
    description: On Leave
    meaning: HL7FHIR:onleave
  HL7FHIR:finished:
    text: HL7FHIR:finished
    description: Finished
    meaning: HL7FHIR:finished
  HL7FHIR:cancelled:
    text: HL7FHIR:cancelled
    description: Cancelled
    meaning: HL7FHIR:cancelled
  HL7FHIR:entered-in-error:
    text: HL7FHIR:entered-in-error
    description: Entered in Error
    meaning: HL7FHIR:entered-in-error
  HL7FHIR:unknown:
    text: HL7FHIR:unknown
    description: Unknown
    meaning: HL7FHIR:unknown

```
</details>

</div>