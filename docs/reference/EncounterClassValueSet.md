---
search:
  boost: 2.0
---


# Enum: EncounterClassValueSet 




_Permitted codes for Encounter Class Value Set v2.0.0 (value set HL7FHIR:encounter.class)._



<div data-search-exclude markdown="1">

URI: [rdcdm:EncounterClassValueSet](https://github.com/BIH-CEI/rd-cdm/EncounterClassValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| HL7FHIR:AMB | HL7FHIR:AMB | Ambulatory |
| HL7FHIR:IMP | HL7FHIR:IMP | Inpatient |
| HL7FHIR:OBSENC | HL7FHIR:OBSENC | Observation |
| HL7FHIR:EMER | HL7FHIR:EMER | Emergency |
| HL7FHIR:VR | HL7FHIR:VR | Virtual |
| HL7FHIR:HH | HL7FHIR:HH | Home Health |
| CustomCode:RDC | CustomCode:RDC | RD Specialist Center |
| SNOMEDCT:261665006 | SNOMEDCT:261665006 | Unknown |




## Slots

| Name | Description |
| ---  | --- |
| [4.4_Encounter_Class](4.4_Encounter_Class.md) | The class of an encounter of the individualat the time of data capture |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: EncounterClassValueSet
description: Permitted codes for Encounter Class Value Set v2.0.0 (value set HL7FHIR:encounter.class).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  HL7FHIR:AMB:
    text: HL7FHIR:AMB
    description: Ambulatory
    meaning: HL7FHIR:AMB
  HL7FHIR:IMP:
    text: HL7FHIR:IMP
    description: Inpatient
    meaning: HL7FHIR:IMP
  HL7FHIR:OBSENC:
    text: HL7FHIR:OBSENC
    description: Observation
    meaning: HL7FHIR:OBSENC
  HL7FHIR:EMER:
    text: HL7FHIR:EMER
    description: Emergency
    meaning: HL7FHIR:EMER
  HL7FHIR:VR:
    text: HL7FHIR:VR
    description: Virtual
    meaning: HL7FHIR:VR
  HL7FHIR:HH:
    text: HL7FHIR:HH
    description: Home Health
    meaning: HL7FHIR:HH
  CustomCode:RDC:
    text: CustomCode:RDC
    description: RD Specialist Center
    meaning: CustomCode:RDC
  SNOMEDCT:261665006:
    text: SNOMEDCT:261665006
    description: Unknown
    meaning: SNOMEDCT:261665006

```
</details>

</div>