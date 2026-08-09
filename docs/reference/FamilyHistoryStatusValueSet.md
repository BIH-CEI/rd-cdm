---
search:
  boost: 2.0
---


# Enum: FamilyHistoryStatusValueSet 




_Permitted codes for FamilyHistoryStatus Value Set v2.0.0 (value set HL7FHIR:familymemberhistory.status)._



<div data-search-exclude markdown="1">

URI: [rdcdm:FamilyHistoryStatusValueSet](https://github.com/BIH-CEI/rd-cdm/FamilyHistoryStatusValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| HL7FHIR:partial | HL7FHIR:partial | Partial |
| HL7FHIR:completed | HL7FHIR:completed | Completed |
| HL7FHIR:entered-in-error | HL7FHIR:entered-in-error | Entered in Error |
| HL7FHIR:health-unknown | HL7FHIR:health-unknown | Health Unknown |




## Slots

| Name | Description |
| ---  | --- |
| [6.4.6_Family_Member_Record_Status](6.4.6_Family_Member_Record_Status.md) | Specifies the record’s status of the family history of a specific family memb... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: FamilyHistoryStatusValueSet
description: Permitted codes for FamilyHistoryStatus Value Set v2.0.0 (value set HL7FHIR:familymemberhistory.status).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  HL7FHIR:partial:
    text: HL7FHIR:partial
    description: Partial
    meaning: HL7FHIR:partial
  HL7FHIR:completed:
    text: HL7FHIR:completed
    description: Completed
    meaning: HL7FHIR:completed
  HL7FHIR:entered-in-error:
    text: HL7FHIR:entered-in-error
    description: Entered in Error
    meaning: HL7FHIR:entered-in-error
  HL7FHIR:health-unknown:
    text: HL7FHIR:health-unknown
    description: Health Unknown
    meaning: HL7FHIR:health-unknown

```
</details>

</div>