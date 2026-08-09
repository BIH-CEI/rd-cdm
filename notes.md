# RD-CDM v2.1.0

Full changelog: https://rd-cdm.readthedocs.io/en/latest/changelog.html

## ⚠️ Changes affecting data capture

**Two SNOMED CT codes are withdrawn from new capture.** Neither resolves in the
SNOMED CT submission BioPortal currently publishes (`2025_09_01`), and BioPortal
is this model's terminology authority.

| Code | Label | Value sets | Replaced by |
|---|---|---|---|
| `SNOMEDCT:184115007` | Patient sex unknown | Sex at Birth, AdministrativeGender | `SNOMEDCT:261665006` *Unknown* |
| `SNOMEDCT:185924006` | Unknown - Opted-out | Vital Status | `SNOMEDCT:261665006` *Unknown* |

Both **remain in their value sets**, marked `status: inactive` with
`replacedBy`. Identifiers are never reused, so a record captured against one
still means what it meant when it was recorded — removing them would make
existing data uninterpretable and force a migration. Generators building a form
or dropdown should filter to `status: active`.

`SNOMEDCT:261665006` *Unknown* is **added as a member** of both sex value sets,
which otherwise offered no active "unknown" option (`1220561009` *Not recorded*
is a statement about the record, not about the person). For downstream models
such as RareLink this is an additive dropdown option, not a data migration.

**Twenty ontology labels adopted from BioPortal**, across Karyotypic Sex (9),
Gender Identity (2), Vital Status (2), Age at Onset / Diagnosis (2) and
Reference Genome (5). Every replaced string is preserved in the new
`Coding.displayLabel`, so nothing curated is lost — for example `XX` alongside
`Karyotype 46, XX`, and `GRCh38 (hg38)` alongside `GRCh38`.

> **Note for RareLink and other downstream models:** these labels are copied by
> hand into RareLink's CDM schema definitions and `label_dicts.py`, and are
> emitted as Phenopacket labels. Adopting them there is a separate change and
> will require re-baselining golden files. Prefer `displayLabel` for REDCap
> dropdowns and other data-entry surfaces.

## Added

- **Browsable element reference.** `gen-doc` documents a *schema*, and the
  RD-CDM's data elements and value sets are *instances* — so the generated
  reference described `Coding` and `ValueSet` as abstract shapes and never
  mentioned element 6.1.11 or the codes it permits. The new **`rd-cdm-profile`**
  command projects the instance data into a LinkML schema
  (`schema/rd_cdm_profile.yaml`): value set → enum with `meaning:` on every
  member, data element → slot named by its ordinal with `slot_uri` set to its
  element code, section → class. Published with the package, so consumers can
  import the value sets as bound LinkML enumerations instead of re-declaring
  them.
- **New data element 6.4.0 Family Identifier** (`GA4GH:family.id`, FHIR
  `Group.identifier`, Phenopacket `Family.id`). Numbered 6.4.0 so no existing
  ordinal in section 6.4 shifts. Required by RareLink for Family Phenopacket
  export (BIH-CEI/rarelink#219).
- **Element 2.5 renamed** from *Country of Birth* to **Country of Origin**,
  aligned with the equivalent GDI element (descent or lineage; ISO 3166-1 /
  3166-2). Now `CustomCode:country_of_origin` — the SNOMED concept denotes
  country of *birth*, which is not descent.
- **`Coding.displayLabel`, `.status`, `.replacedBy`, `.statusNote`** and the
  `CodeStatus` enum.
- **Offline structural validation** — `rd-cdm-validate --offline` needs no
  BioPortal key and runs in CI on every pull request. It enforces that value
  sets are declared once under a unique id and label, that every reference
  resolves, that a `replacedBy` target is a member of the same value set, that
  section labels are consistent, and that **a value set's `id` is the CURIE of
  the data element it constrains**.
- **Dependabot** for `pip` and `github-actions`.

## Fixed

- **Two value sets were declared twice** — *Vital Status* and *Age Category*
  each appeared verbatim twice, so their members were validated, and reported,
  twice.
- **Two data elements shared one value set label.** 5.9 and 6.2.7 both
  referenced `Severity Value Set v2.0.0`, of which there were two. Split into
  **Disease Severity** (`SNOMEDCT:246112005`) and **Phenotype Severity**
  (`HP:0012824`).
- **Seven value set ids did not identify the element they constrain**, including
  `SNOMEDCT:281053000` — the deprecated Sex-at-Birth concept the model moved off
  in v2.0.3 — and two LOINC codes carrying `SNOMEDCT` and `HL7FHIR` prefixes.
  Data elements reference value sets by *label*, so nothing ever resolved the
  `id` and a stale one was invisible.
- **Section labels were inconsistent**: 6.1.x said `6. Genetic Findings`, 6.2.x
  mixed `6.` and `6.2`, and section 6.4 split six elements as `6.4 Family
  History` against eight as `6.4 Family`.
- **A `400` from BioPortal aborted the entire validation run.** Only `404` was
  treated as "not found", but the bare-identifier fallback used for SNOMEDCT,
  LOINC and ICD10CM is not a well-formed IRI and returns `400`.
- **`VS X: missing member Y` was misleading** — it described a live resolution
  failure but read as a membership failure. Now `VS X: unresolvable code Y`.
- **A placeholder version could overwrite a real one.** `rd-cdm-sync-versions`
  replaced Sequence Ontology `2.6` with the string `unknown`, which no later run
  could undo.
- **Version and label lookups used different BioPortal submissions** — HGNC
  labels resolve against `HGNC-NR` while the version was read from `HGNC`.
- **The schema could not be loaded by LinkML's own tooling.** A top-level
  `date:` key is not a `SchemaDefinition` slot, so `linkml validate` and
  `gen-doc` failed before doing any work. The release date is now
  `annotations.rd_cdm_date`.
- **CI was failing at its install step** — `poetry install --with dev` treats
  `dev` and `test` as dependency *groups*; they are *extras*.
- **Committed generated files are now checked against their sources in CI**, so
  a stale artefact cannot be published.

## Open for v2.2.0

Vital Status loses the opted-out *reason* when `185924006` migrates to the
generic *Unknown*. Representing it belongs in the consent section (7.x) rather
than in vital status.
