---
search:
  boost: 2.0
---


# Enum: DiseaseSeverityValueSet 




_Permitted codes for Disease Severity Value Set v2.0.0 (value set SNOMEDCT:246112005)._



<div data-search-exclude markdown="1">

URI: [rdcdm:DiseaseSeverityValueSet](https://github.com/BIH-CEI/rd-cdm/DiseaseSeverityValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| SNOMEDCT:24484000 | SNOMEDCT:24484000 | Severe |
| SNOMEDCT:6736007 | SNOMEDCT:6736007 | Moderate severity |
| SNOMEDCT:255604002 | SNOMEDCT:255604002 | Mild |




## Slots

| Name | Description |
| ---  | --- |
| [5.9_Severity](5.9_Severity.md) | The severity of the disease is categorised byclinical evaluation |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: DiseaseSeverityValueSet
description: Permitted codes for Disease Severity Value Set v2.0.0 (value set SNOMEDCT:246112005).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  SNOMEDCT:24484000:
    text: SNOMEDCT:24484000
    description: Severe
    meaning: SNOMEDCT:24484000
  SNOMEDCT:6736007:
    text: SNOMEDCT:6736007
    description: Moderate severity
    meaning: SNOMEDCT:6736007
  SNOMEDCT:255604002:
    text: SNOMEDCT:255604002
    description: Mild
    meaning: SNOMEDCT:255604002

```
</details>

</div>