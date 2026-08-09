# Changelog

!!! tip
    The RD-CDM paper has now been published at Nature Scientific Data. You can
    read it [here](https://www.nature.com/articles/s41597-025-04558-z)!

This changelog provides a history of the changes to the RD-CDM.

!!! note
    Previous versions (v1.0 – v1.7) were developed in a German context and are
    not publicly available.

---

## v2.1.0 (2026-08-08)

### New Data Element: Family Identifier (6.4.0)

A new data element **6.4.0 Family Identifier** has been added to section 6.4
Family History:

| Property | Value |
|---|---|
| Element code | `GA4GH:family.id` |
| Data type | Identifier |
| FHIR | `Group.identifier` |
| Phenopacket Schema | `Family.id` |

It identifies the family as a whole — the group shared by an individual and
their relatives — and complements **6.4.1 Family Member Pseudonym**, which
identifies a single member. It is coded under GA4GH, matching the convention
already used for other Phenopacket-derived elements (6.1.2, 6.2.8, 6.2.9),
because the element exists to carry the Phenopacket `Family.id` rather than an
independent clinical concept.

The element was numbered **6.4.0** deliberately, so that no existing ordinal in
section 6.4 shifts — downstream models reference elements by ordinal.

Required by RareLink for Family Phenopacket export
([BIH-CEI/rarelink#219](https://github.com/BIH-CEI/rarelink/issues/219)).

### Data Element Update: Country of Origin (2.5)

Data element **2.5** has been renamed from *Country of Birth* to **Country of
Origin** and aligned with the equivalent GDI element:

- **Definition**: a person's descent or lineage, from a person or from a
  population.
- **Data specification**: a 2- or 3-letter code from **ISO 3166-1** where only a
  country is provided; a value from **ISO 3166-2** where a country subdivision
  is provided.

!!! note
    The element code changed from SNOMED CT `370159000 | Country of birth |` to
    `CustomCode:country_of_origin`. The SNOMED concept denotes *country of
    birth*, which is not the same as descent or lineage — a person born in one
    country may have their origin in another. No SNOMED concept was found that
    matches the GDI definition precisely: `372148003 | Ethnic group |` and
    `103579009 | Race |` are both narrower and would misrepresent the element.
    `CustomCode` follows the convention already used for elements 7.4, 7.5, 7.7
    and 8.1, where no clean ontology match exists. If a suitable SNOMED or GDI
    concept is identified, this should be replaced.

### Ontology Terms Withdrawn from New Capture

Two SNOMED CT codes no longer resolve in the submission BioPortal currently
publishes (`2025_09_01`). Since BioPortal is this model's terminology authority,
both are marked `status: inactive` and are **not** offered for new data capture:

| Code | Label | Value sets | Replaced by |
|---|---|---|---|
| `SNOMEDCT:184115007` | Patient sex unknown | Sex at Birth, AdministrativeGender | `SNOMEDCT:261665006` *Unknown* |
| `SNOMEDCT:185924006` | Unknown - Opted-out | Vital Status | `SNOMEDCT:261665006` *Unknown* |

Both codes **remain in their value sets**. Identifiers are never reused, so a
record captured against one still means exactly what it meant when it was
recorded; removing them would make existing data uninterpretable and force a
migration. `rd-cdm-validate` reports them as known inactivations rather than
errors, and warns if either starts resolving again.

!!! note
    `SNOMEDCT:261665006` *Unknown* has been **added as a member** of both sex
    value sets, which otherwise offered no active "unknown" option —
    `1220561009` *Not recorded* is a statement about the record, not about the
    person. For downstream models such as RareLink this is an additive dropdown
    option, not a data migration.

    For Vital Status, the opted-out *reason* is not preserved by the migration.
    Representing it belongs in the consent section (7.x) rather than in vital
    status, and is open for v2.2.0.

### New Schema Fields: `displayLabel`, `status`, `replacedBy`

`Coding` gains four optional attributes:

- **`displayLabel`** — a presentation label for forms and user interfaces, used
  where the terminology's preferred label is unhelpful to a data entrant. Never
  validated against the terminology.
- **`status`** (`CodeStatus`: `active` | `inactive`) — whether the code still
  resolves against BioPortal.
- **`replacedBy`** — the active code a value recorded under an inactive one
  migrates to. Must itself be a member of the same value set.
- **`statusNote`** — why a code carries a non-default status.

`label` now means *the preferred label in the source terminology* and is what
`rd-cdm-validate` compares.

### Ontology Labels Adopted from BioPortal

Twenty codes whose recorded label had drifted now carry the terminology's
preferred label. Every replaced string is preserved as `displayLabel`, so
nothing curated is lost:

| Value set | `label` now | `displayLabel` (was `label`) |
|---|---|---|
| Karyotypic Sex (9 codes) | Karyotype 46, XX … | XX … |
| Gender Identity (2) | Identifies as female gender | Female gender identity |
| Vital Status (2) | Lost to follow-up; Unknown | Unknown - Lost in follow-up; Unknown - Other Reason |
| Age at Onset / Diagnosis (2) | Prenatal finding | Prenatal |
| Reference Genome (5) | GRCh38 … | GRCh38 (hg38) … |

!!! warning
    RareLink copies these labels by hand into its CDM schema definitions and
    `label_dicts.py`, and emits them as Phenopacket labels. Adopting them there
    is a separate change and will require re-baselining RareLink's golden files.
    Prefer `displayLabel` for REDCap dropdowns and other data-entry surfaces.

### Value Set Corrections

- **Two value sets were declared twice.** *Vital Status*
  (`SNOMEDCT:278844005`) and *Age Category* (`SNOMEDCT:105727008`) each appeared
  verbatim twice, so their members were validated — and reported — twice.
- **Two data elements shared one value set label.** *5.9 Severity* and
  *6.2.7 Severity* both referenced `Severity Value Set v2.0.0`, of which there
  were two. Split into **Disease Severity Value Set** (`SNOMEDCT:246112005`) and
  **Phenotype Severity Value Set** (`HP:0012824`).
- **Seven value set ids did not identify the element they constrain.** Data
  elements reference value sets by *label*, so nothing ever resolved the `id`
  and a stale one was invisible:

    | Value set | Was | Now |
    |---|---|---|
    | Sex at Birth | `SNOMEDCT:281053000` | `LOINC:76689-9` |
    | AdministrativeGender | `SNOMEDCT:54123-5` | `LOINC:54123-5` |
    | Verification Status | `HL7FHIR:99498-8` | `LOINC:99498-8` |
    | Consent Status | `HL7FHIR:309370004` | `SNOMEDCT:309370004` |
    | Phenotype Status | `CustomCode:phenotypicfeature.excluded` | `SNOMEDCT:363778006` |
    | Contact for Research | `SNOMEDCT:consent_contact_research` | `CustomCode:consent_contact_research` |
    | Data Reuse Consent | `SNOMEDCT:conset_data_reuse` | `CustomCode:consent_data_reuse` |

    `SNOMEDCT:281053000` is the deprecated Sex-at-Birth concept the model moved
    off in v2.0.3 (see below); `54123-5` and `99498-8` are LOINC codes that
    carried a `SNOMEDCT` and an `HL7FHIR` prefix respectively. The typo in
    `CustomCode:conset_data_reuse` (element 7.5) is also corrected.

- **Section labels are now consistent.** Elements 6.1.x said
  `6. Genetic Findings`, 6.2.x mixed `6.` and `6.2`, and section 6.4 split six
  elements as `6.4 Family History` against eight as `6.4 Family`.

### Offline Structural Validation

`rd-cdm-validate --offline` runs a set of consistency checks that need no
BioPortal key, and therefore run in CI on every pull request:

- value sets are declared once, under a unique id **and** a unique label;
- every referenced value set exists and every declared one is used;
- members are not duplicated, and a value set is not entirely inactive;
- a `replacedBy` target is a member of the same value set;
- section labels are consistent within an ordinal group;
- **a value set's `id` is the CURIE of the data element it constrains**.

That last invariant is what would have caught `SNOMEDCT:281053000` when element
2.2 moved to LOINC in v2.0.3.

### Browsable Element Reference

`gen-doc` documents a *schema*, and the RD-CDM's data elements and value sets
are *instances* of the five-class container — so the generated reference
described `Coding` and `ValueSet` as abstract shapes and never mentioned element
6.1.11 or the codes it permits.

The new **`rd-cdm-profile`** command projects the instance data into a LinkML
schema (`schema/rd_cdm_profile.yaml`) where each value set is an enumeration
with `meaning:` on every member, each data element a slot named by its ordinal
with `slot_uri` set to its element code, and each section a class. Stock
`gen-doc` then renders the whole model. See the
[Element Reference](reference/index.md) for the elements and value sets, and the
[Data Model Reference](datamodel/index.md) for the container schema.

The generated schema is published with the package, so downstream consumers can
import the value sets as bound LinkML enumerations rather than re-declaring
them.

### Documentation moved to MkDocs

These docs are now built with MkDocs and the Material theme rather than Sphinx.
LinkML's `gen-doc` templates are written for mkdocs-material — they use its
search boosting, admonitions and collapsible blocks — and rendered poorly under
the Sphinx theme, which mattered once the generated reference grew past a
hundred pages. Nothing was dropped in the move.

### Ontology Drift Automation

`rd-cdm-validate` was never invoked by any workflow. The scheduled CI job ran
merge, class generation and `linkml validate`, but not the BioPortal check — so
version and label drift had gone undetected despite the weekly schedule and a
configured API key.

A dedicated **Ontology drift** workflow now runs weekly:

1. `rd-cdm-sync-versions` applies code system **version** drift automatically.
2. `rd-cdm-merge` / `-profile` / `-json` / `-csv` regenerate the derived files.
3. `rd-cdm-validate` reports label drift and unresolvable codes.
4. A pull request is opened — or, on re-runs, **updated** — with the findings.

Label drift and unresolvable codes are deliberately **not** applied
automatically: a changed or absent label can mean a term was redefined or
withdrawn, which is a data question rather than housekeeping.

The new `rd-cdm-sync-versions` command can also be run locally:

```bash
export BIOPORTAL_API_KEY=...
rd-cdm-sync-versions
```

### Validation and Tooling Fixes

- **A `400` from BioPortal aborted the entire validation run.**
  `get_remote_label` treated only `404` as "not found", but the bare-identifier
  fallback used for SNOMEDCT, LOINC and ICD10CM is not a well-formed IRI and
  returns `400` — so the first unresolvable code raised instead of being
  recorded.
- **`VS X: missing member Y` was misleading.** The message described a live
  BioPortal resolution failure but read as a value set *membership* failure. It
  is now `VS X: unresolvable code Y`.
- **A placeholder version could overwrite a real one.**
  `rd-cdm-sync-versions` replaced Sequence Ontology `2.6` with the string
  `unknown`, which no later run could undo. Placeholders are now reported and
  skipped.
- **Version and label lookups used different BioPortal submissions.** HGNC
  labels resolve against `HGNC-NR` while the version was read from `HGNC`.
- **The schema could not be loaded by LinkML's own tooling.** A top-level
  `date:` key is not a `SchemaDefinition` slot, so `linkml validate` and
  `gen-doc` failed before doing any work. The release date is now
  `annotations.rd_cdm_date`. This also removes the workaround in
  `gen_pydantic.py` that stripped the key into a temporary file — which is why
  class generation had kept working while validation did not.
- **CI was failing at its install step.** `poetry install --with dev` treats
  `dev` and `test` as dependency *groups*; they are *extras*. The
  merge-and-validate and ontology-drift jobs never ran, and the test job never
  installed `pytest`.
- **The ontology drift report could not distinguish a clean result from a
  crash.** A failed validation run produced an empty findings section rather
  than an alert.
- **Committed generated files are now checked against their sources in CI**, so
  a stale artefact cannot be published to PyPI.

### Single Source of Truth for the Model Version

`schema/rd_cdm.yaml` declares the model version; `rd-cdm-merge` propagates it
into `instances/rd_cdm.yaml` and the generated JSON and CSV exports. This was
already the intended design, but `versioning.get_model_version()` did not
implement it — it called an undefined `_read_project_version` and looked for
`pyproject.toml` inside `src/`, so any caller would have raised `NameError`. It
now reads the schema.

`pyproject.toml` still carries its own copy of the version because packaging
requires it. `tests/test_version_consistency.py` now fails if the two disagree,
or if the merged instance is stale relative to the schema.

### Dependency Automation

Dependabot has been enabled for `pip` and `github-actions`, with LinkML packages
and development tooling grouped so related updates arrive as a single pull
request.

---

## v2.0.3 (2026-03-24)

### Code System Version Updates

All ontology and code system versions have been updated to their latest releases
as reported by BioPortal. The following version drifts were resolved:

| Code System | Previous Version | Updated Version |
|---|---|---|
| SNOMEDCT | SNOMEDCT_US_2024_09_01 | 2025AB |
| LOINC | LNC278 | 281 |
| HP | 2025-05-06 | 2026-02-16 |
| NCIT | 24.01e | 26.02d |
| NCBITAXON | NCBI2024_04_02 | 2025_04_10 |
| GENO | 2023-10-08 | 2026-02-02 |
| UO | 2023-05-25 | 2026-01-16 |
| ECO | 2025-06-23 | releases/2025-06-23 |
| ICD10CM | ICD10CM_2025 | 2026 |
| MONDO | 2025-06-03 | 2026-03-03 |
| ORDO | 4.7 | 4.8 |

### Data Element Update: Sex at Birth (2.2)

The code for data element **2.2 Sex at Birth** has been updated. The previous
SNOMED CT concept `281053000 | Sex of baby at delivery (observable entity)` was
identified as inactive (deprecated) in the SNOMED CT browser.

The element is now coded using the LOINC concept:

- **LOINC 76689-9** — *Sex assigned at birth*

This aligns with HL7 FHIR's `Patient` resource and is semantically precise as a
question/observable code. The value set choices (Female, Male, Unknown, etc.)
remain SNOMED CT encoded as before.

### Repository and Package Structure Refactor

The versioned folder structure inside `src/rd_cdm/instances/` has been removed.
Previously, each data model version occupied a dedicated subdirectory (e.g.
`instances/v2_0_2/`) with the version repeated in filenames (e.g.
`rd_cdm_v2_0_2.yaml`). This created redundancy since Git tags and PyPI
versioning already serve as the version archive.

**New structure:**

```text
src/rd_cdm/
├── schema/
│   └── rd_cdm.yaml          # LinkML schema — version defined here
├── instances/
│   ├── code_systems.yaml
│   ├── data_elements.yaml
│   ├── value_sets.yaml
│   └── rd_cdm.yaml          # merged, version-stamped output
│   ├── jsons/
│   │   └── rd_cdm.json
│   └── csvs/
│       ├── code_systems.csv
│       ├── data_elements.csv
│       ├── value_sets.csv
│       └── rd_cdm.csv
```

**Version is now embedded in every exported file.** The fields `rd_cdm_version`
and `rd_cdm_date` are defined in the LinkML schema (`schema/rd_cdm.yaml`) and
written into every merged and exported file by `rd-cdm-merge`. Every standalone
YAML, JSON, or CSV file is therefore self-describing.

To use an older version of the model, use the corresponding Git tag or pin the
PyPI package:

```bash
pip install rd-cdm==2.0.2
```

### CLI Naming Update

All CLI commands have been renamed from `rdcdm-*` to `rd-cdm-*` for consistency
with the PyPI package name `rd-cdm`:

| Old command | New command |
|---|---|
| `rdcdm-merge` | `rd-cdm-merge` |
| `rdcdm-json` | `rd-cdm-json` |
| `rdcdm-csv` | `rd-cdm-csv` |
| `rdcdm-validate` | `rd-cdm-validate` |

The `--version` / `-v` argument has been removed from all CLI tools since
version resolution via subdirectories is no longer needed.

### Validation Improvements

The `rd-cdm-validate` command now shows progress bars (via `tqdm`) for each of
the three validation phases: code system version checking, data element
validation, and value set code validation. The current element being checked is
shown in the progress bar postfix.

The validation summary now reports the data model version at the top:

```text
=== RD-CDM VALIDATION SUMMARY (model version: 2.0.3) ===
```

### Dependency Changes

The following dependencies were removed as they were not used by the package:
`numpy`, `requests-cache`, `jsonschema`, `oaklib`.

`linkml` has been moved from a core runtime dependency to an optional `dev`
extra, since it is only needed to regenerate the Python classes from the schema.
Users installing `rd-cdm` for data access do not require it:

```bash
pip install rd-cdm        # no linkml
pip install rd-cdm[dev]   # includes linkml for schema development
```

`tqdm` has been added as a core dependency for validation progress reporting.

### Python Class Generation

The `gen_pydantic.py` utility now generates both output files from the schema in
a single run:

- `src/rd_cdm/python_classes/rd_cdm.py` — LinkML runtime dataclasses (via
  `PythonGenerator`)
- `src/rd_cdm/python_classes/rd_cdm_pydantic.py` — Pydantic v2 models (via
  `PydanticGenerator`)

Custom top-level schema fields (`date`) that are not valid `SchemaDefinition`
fields were stripped into a temporary file before generation to avoid
`SchemaDefinition.__init__()` errors. *(Removed in v2.1.0, where the date became
an annotation.)*

---

## v2.0.1 & v2.0.2 (2025-08-07)

**What's new**

- **Complete LinkML model definition** polished and consolidated for RD-CDM
  v2.0.1.
    - `Coding`, `ValueSet`, `DataElement`, and `CodeSystem` clarified and
      aligned.
    - `elementCode.system` and `CodeSystem.id` now consistently use ontology
      acronyms (e.g. `SNOMEDCT`, `LOINC`, `HP`, `NCIT`).
- **Automated validation against BioPortal** (new CLI: `rd-cdm-validate`).
    - Validates all `DataElement.elementCode` and `ValueSet.codes` entries
      against the **latest** BioPortal content.
    - Summarizes results: number of data elements and value set members checked,
      valid/missing/skipped terms, label-drift warnings.
    - **Label drift** (model label ≠ live `prefLabel`) is reported as a
      **warning**, not a failure.
    - **Composite SNOMED expressions** (codes containing `=`) are **skipped** on
      purpose.
    - Handles LOINC part/answer codes (e.g. `LA26406-1`) and NCIt IRIs via the
      EVS Thesaurus mapping.
    - Uses an explicit ontology mapping (HP/MONDO/OBO, NCIT/EVS, SNOMEDCT,
      LOINC, etc.) plus CURIE and IRI fallbacks.
- **Version checks (live vs. model)**
    - By default checks every `CodeSystem` in the instance directory against
      BioPortal's `latest_submission`.
    - A configurable **skip list** excludes non-ontology systems (e.g.
      `CustomCode`, `GA4GH`, `HL7FHIR`) from version drift checks.
    - Environment variable `BIOPORTAL_API_KEY` is required.
- **Dynamic instance version resolution** — validation and merge tooling
  auto-locate the latest instances directory.
- **Merge improvements** — `merge_instances.py` reliably rebuilds
  `rd_cdm_full.yaml` from `code_systems.yaml`, `data_elements.yaml`, and
  `value_sets.yaml`.
- **Export utilities** — helpers to export LinkML instances to **JSON** and
  **CSV** for downstream processing.

**Data and label consistency updates**

- Adjusted several labels to match BioPortal `prefLabel`, e.g. SNOMED CT
  `410605003` → "Confirmed present"; HPO onset labels simplified to BioPortal's
  canonical forms.
- Ensured validation uses `ValueSet.codes` (the members) rather than the
  ValueSet `id` itself.

**CodeSystem version alignment**

Code system versions updated to BioPortal's current `latest_submission`: **HP**
→ `hp/releases/2025-05-06`, **SNOMEDCT** → `SNOMEDCT_US_2024_09_01`, **LOINC** →
`LNC278`, **NCIT** → `24.01e`.

**Breaking / behavioral notes**

- `elementCode.system` must match a `CodeSystem.id`.
- Validation of SNOMED CT post-coordination / ECL (codes containing `=`) is
  skipped.
- Version checks intentionally exclude systems in the skip list.

---

## v2.0.0 (2025-02-08)

The RD-CDM has been updated to version 2.0.0 as the corresponding manuscript was
published.

---

## v2.0.0.dev0 (2024-09-30)

Initial release of the RD-CDM in development and review.
