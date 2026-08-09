---
search:
  boost: 2.0
---


# Enum: VerificationStatusValueSet 




_Permitted codes for Verification Status Value Set v2.0.0 (value set LOINC:99498-8)._



<div data-search-exclude markdown="1">

URI: [rdcdm:VerificationStatusValueSet](https://github.com/BIH-CEI/rd-cdm/VerificationStatusValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| HL7FHIR:unconfirmed | HL7FHIR:unconfirmed | Unconfirmed |
| HL7FHIR:provisional | HL7FHIR:provisional | Provisional |
| HL7FHIR:differential | HL7FHIR:differential | Differential |
| HL7FHIR:confirmed | HL7FHIR:confirmed | Confirmed |
| HL7FHIR:refuted | HL7FHIR:refuted | Refuted |
| HL7FHIR:entered-in-error | HL7FHIR:entered-in-error | Entered in Error |




## Slots

| Name | Description |
| ---  | --- |
| [5.2_Verification_Status](5.2_Verification_Status.md) | The verification status of the disease |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: VerificationStatusValueSet
description: Permitted codes for Verification Status Value Set v2.0.0 (value set LOINC:99498-8).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  HL7FHIR:unconfirmed:
    text: HL7FHIR:unconfirmed
    description: Unconfirmed
    meaning: HL7FHIR:unconfirmed
  HL7FHIR:provisional:
    text: HL7FHIR:provisional
    description: Provisional
    meaning: HL7FHIR:provisional
  HL7FHIR:differential:
    text: HL7FHIR:differential
    description: Differential
    meaning: HL7FHIR:differential
  HL7FHIR:confirmed:
    text: HL7FHIR:confirmed
    description: Confirmed
    meaning: HL7FHIR:confirmed
  HL7FHIR:refuted:
    text: HL7FHIR:refuted
    description: Refuted
    meaning: HL7FHIR:refuted
  HL7FHIR:entered-in-error:
    text: HL7FHIR:entered-in-error
    description: Entered in Error
    meaning: HL7FHIR:entered-in-error

```
</details>

</div>