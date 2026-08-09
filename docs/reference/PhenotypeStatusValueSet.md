---
search:
  boost: 2.0
---


# Enum: PhenotypeStatusValueSet 




_Permitted codes for Phenotype Status Value Set v2.0.0 (value set SNOMEDCT:363778006)._



<div data-search-exclude markdown="1">

URI: [rdcdm:PhenotypeStatusValueSet](https://github.com/BIH-CEI/rd-cdm/PhenotypeStatusValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| SNOMEDCT:410605003 | SNOMEDCT:410605003 | Confirmed present |
| SNOMEDCT:723511001 | SNOMEDCT:723511001 | Refuted |




## Slots

| Name | Description |
| ---  | --- |
| [6.2.2_Status](6.2.2_Status.md) | The current status of the phenotypic feature, indicating whether it is confir... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: PhenotypeStatusValueSet
description: Permitted codes for Phenotype Status Value Set v2.0.0 (value set SNOMEDCT:363778006).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  SNOMEDCT:410605003:
    text: SNOMEDCT:410605003
    description: Confirmed present
    meaning: SNOMEDCT:410605003
  SNOMEDCT:723511001:
    text: SNOMEDCT:723511001
    description: Refuted
    meaning: SNOMEDCT:723511001

```
</details>

</div>