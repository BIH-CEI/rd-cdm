---
search:
  boost: 2.0
---


# Enum: ConsentStatusValueSet 




_Permitted codes for Consent Status Value Set v2.0.0 (value set SNOMEDCT:309370004)._



<div data-search-exclude markdown="1">

URI: [rdcdm:ConsentStatusValueSet](https://github.com/BIH-CEI/rd-cdm/ConsentStatusValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| HL7FHIR:draft | HL7FHIR:draft | Pending |
| HL7FHIR:proposed | HL7FHIR:proposed | Proposed |
| HL7FHIR:active | HL7FHIR:active | Active |
| HL7FHIR:rejected | HL7FHIR:rejected | Rejected |
| HL7FHIR:inactive | HL7FHIR:inactive | Inactive |
| HL7FHIR:entered-in-error | HL7FHIR:entered-in-error | Entered in Error |




## Slots

| Name | Description |
| ---  | --- |
| [7.1_Consent_Status](7.1_Consent_Status.md) | Indicates the current status of the consent |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: ConsentStatusValueSet
description: Permitted codes for Consent Status Value Set v2.0.0 (value set SNOMEDCT:309370004).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  HL7FHIR:draft:
    text: HL7FHIR:draft
    description: Pending
    meaning: HL7FHIR:draft
  HL7FHIR:proposed:
    text: HL7FHIR:proposed
    description: Proposed
    meaning: HL7FHIR:proposed
  HL7FHIR:active:
    text: HL7FHIR:active
    description: Active
    meaning: HL7FHIR:active
  HL7FHIR:rejected:
    text: HL7FHIR:rejected
    description: Rejected
    meaning: HL7FHIR:rejected
  HL7FHIR:inactive:
    text: HL7FHIR:inactive
    description: Inactive
    meaning: HL7FHIR:inactive
  HL7FHIR:entered-in-error:
    text: HL7FHIR:entered-in-error
    description: Entered in Error
    meaning: HL7FHIR:entered-in-error

```
</details>

</div>