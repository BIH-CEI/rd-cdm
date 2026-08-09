---
search:
  boost: 2.0
---


# Enum: TherapeuticActionabilityValueSet 




_Permitted codes for Therapeutic Actionability Value Set v2.0.0 (value set GA4GH:therapeutic_actionability)._



<div data-search-exclude markdown="1">

URI: [rdcdm:TherapeuticActionabilityValueSet](https://github.com/BIH-CEI/rd-cdm/TherapeuticActionabilityValueSet)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| GA4GH:UNKNOWN_ACTIONABILITY | GA4GH:UNKNOWN_ACTIONABILITY | There is not enough information at this time to support any therapeutic actio... |
| GA4GH:NOT_ACTIONABLE | GA4GH:NOT_ACTIONABLE | This variant has no therapeutic actionability |
| GA4GH:ACTIONABLE | GA4GH:ACTIONABLE | This variant is known to be therapeuticallyactionalbe |




## Slots

| Name | Description |
| ---  | --- |
| [6.1.15_Therapeutic_Actionability](6.1.15_Therapeutic_Actionability.md) | An enumeration flagging the variant as being a candidate for treatment or cli... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml






## LinkML Source

<details>
```yaml
name: TherapeuticActionabilityValueSet
description: Permitted codes for Therapeutic Actionability Value Set v2.0.0 (value
  set GA4GH:therapeutic_actionability).
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm_profile.yaml
rank: 1000
permissible_values:
  GA4GH:UNKNOWN_ACTIONABILITY:
    text: GA4GH:UNKNOWN_ACTIONABILITY
    description: There is not enough information at this time to support any therapeutic
      actionability for this variant.
    meaning: GA4GH:UNKNOWN_ACTIONABILITY
  GA4GH:NOT_ACTIONABLE:
    text: GA4GH:NOT_ACTIONABLE
    description: This variant has no therapeutic actionability.
    meaning: GA4GH:NOT_ACTIONABLE
  GA4GH:ACTIONABLE:
    text: GA4GH:ACTIONABLE
    description: This variant is known to be therapeuticallyactionalbe.
    meaning: GA4GH:ACTIONABLE

```
</details>

</div>