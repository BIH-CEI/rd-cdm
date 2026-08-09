---
search:
  boost: 2.0
---


# Enum: CodeStatus 




_Whether a code still resolves against BioPortal, the single terminology authority this model validates against._

__



<div data-search-exclude markdown="1">

URI: [https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/CodeStatus](https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/CodeStatus)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| active | None | The code resolves |
| inactive | None | The code no longer resolves in BioPortal |




## Slots

| Name | Description |
| ---  | --- |
| [status](status.md) | Lifecycle of this code against the model's terminology authority |










## Identifier and Mapping Information





### Schema Source


* from schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml






## LinkML Source

<details>
```yaml
name: CodeStatus
description: 'Whether a code still resolves against BioPortal, the single terminology
  authority this model validates against.

  '
from_schema: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml
rank: 1000
permissible_values:
  active:
    text: active
    description: 'The code resolves. This is the default and is not written out explicitly.

      '
  inactive:
    text: inactive
    description: 'The code no longer resolves in BioPortal. Not available for new
      data capture - use `replacedBy` instead - but retained so that data already
      captured against it stays interpretable. `rd-cdm-validate` reports it as a known
      inactivation rather than an error, and warns if it starts resolving again.

      '

```
</details>

</div>