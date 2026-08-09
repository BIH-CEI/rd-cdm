# Changelog

## v2.1.0 (2026-08-08)

### Added

- **`rd-cdm-profile`** — projects the instance data into a documentable LinkML
  schema (`schema/rd_cdm_profile.yaml`): value set → enum with `meaning:` on
  every member, data element → slot named by its ordinal with `slot_uri` set to
  its element code, section → class. Stock `gen-doc` then renders the elements
  and value sets themselves, which the container schema could never expose.
  Published with the package, so consumers can import the value sets as bound
  LinkML enumerations instead of re-declaring them. Closes #56.

- **Data element 6.4.0 Family Identifier** (`GA4GH:family.id`) — an identifier
  shared by all members of one family, mapping to Phenopacket `Family.id` and
  FHIR `Group.identifier`. It complements 6.4.1 *Family Member Pseudonym*, which
  identifies a single member rather than the family as a whole. Added as 6.4.0 so
  no existing ordinal in section 6.4 shifts. Coded under GA4GH, matching the
  convention already used for Phenopacket-derived elements (6.1.2, 6.2.8, 6.2.9).
  Required by RareLink for Family Phenopacket export
  ([BIH-CEI/rarelink#219](https://github.com/BIH-CEI/rarelink/issues/219)).

- **`rd-cdm-sync-versions`** — applies BioPortal version drift to
  `code_systems.yaml`. Label drift and missing terms are deliberately left for
  review: a changed or absent label can mean a term was redefined or obsoleted,
  which is a data question rather than housekeeping.

- **Weekly ontology-drift workflow** — runs `rd-cdm-sync-versions` and
  `rd-cdm-validate`, then opens or updates a pull request with the findings.
  Re-runs push to the same branch, so drift accumulates in one pull request.

- **Dependabot** for `pip` and `github-actions`.

- **Element 2.5 renamed** from *Country of Birth* to **Country of Origin** and
  aligned with the equivalent GDI element (descent or lineage; ISO 3166-1 or
  3166-2). The element code moved from `SNOMEDCT:370159000 | Country of birth |`
  to `CustomCode:country_of_origin`: the SNOMED concept denotes country of
  *birth*, which is not descent, and no SNOMED concept matches the GDI
  definition precisely. Closes #55.

- **`Coding.displayLabel`** — an optional presentation label for forms and user
  interfaces, for the cases where a terminology's preferred label is unhelpful
  to a data entrant. `label` now tracks the terminology and is what
  `rd-cdm-validate` compares; `displayLabel` carries the curated string. Used to
  keep `XX` alongside `Karyotype 46, XX`, and `GRCh38 (hg38)` alongside `GRCh38`.

- **`Coding.status` / `Coding.replacedBy` / `Coding.statusNote`** (`CodeStatus`:
  `active` | `inactive`) — records that a code no longer resolves against
  BioPortal, the model's terminology authority. An inactive code is **not**
  offered for new capture — a generator building a form from a value set filters
  to `active` — but stays in the value set, with `replacedBy` naming the active
  member a stored value migrates to, so records captured under earlier model
  versions remain interpretable and traceable. `rd-cdm-validate` reports these as
  known inactivations rather than errors, and warns if one starts resolving
  again.

- **Structural validation** (`rd_cdm.utils.structure_checks`, and
  `rd-cdm-validate --offline`) — runs with no BioPortal key. Enforces that value
  sets are declared once under a unique id and label, that every referenced value
  set exists and every declared one is used, that members are not duplicated, and
  that **a value set's `id` is the CURIE of the data element it constrains**.
  Data elements reference value sets by *label*, so nothing resolved the `id`
  and a stale one was invisible. Also checks that no value set is entirely
  inactive, and that a `replacedBy` target is a member of the same value set —
  otherwise a legacy value could not be migrated without leaving it. Covered by
  `tests/test_structure_checks.py`, so it runs in CI where there is no key.

### Fixed

- **Two value sets were declared twice.** `Vital Status` (`SNOMEDCT:278844005`)
  and `Age Category` (`SNOMEDCT:105727008`) each appeared verbatim twice in
  `value_sets.yaml`, so their members were validated — and reported — twice.

- **Two data elements shared one value set label.** *5.9 Severity* and
  *6.2.7 Severity* both referenced `Severity Value Set v2.0.0`, of which there
  were two, distinguishable only by id. Renamed to `Disease Severity Value Set
  v2.0.0` (`SNOMEDCT:246112005`) and `Phenotype Severity Value Set v2.0.0`
  (`HP:0012824`).

- **Seven value set ids did not identify the element they constrain**, having
  been left behind by earlier recodings or written under the wrong prefix:

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
  off in 2.0.3; `54123-5` and `99498-8` are LOINC codes that carried a
  `SNOMEDCT` and an `HL7FHIR` prefix respectively.

- **`CustomCode:conset_data_reuse` typo** in the element code of *7.5 Consent to
  the Reuse of Data*, now `consent_data_reuse`. `CustomCode` is our own
  namespace and no downstream consumer resolves this string — RareLink models
  the element as `rarelink_consent_data`.

- **Two SNOMED CT codes no longer resolve** in the submission BioPortal now
  publishes (`2025_09_01`): `184115007` *Patient sex unknown* (Sex at Birth,
  AdministrativeGender) and `185924006` *Unknown - Opted-out* (Vital Status).
  Since BioPortal is the model's terminology authority, both are marked
  `status: inactive` and withdrawn from new capture, with
  `replacedBy: SNOMEDCT:261665006` *Unknown* — the code already used for this
  purpose across ten other value sets. Both remain in their value sets so
  existing records stay traceable.

  ⚠️ `SNOMEDCT:261665006` is **added as a member** of the two sex value sets,
  which previously had no active "unknown" option once `184115007` is excluded
  (`1220561009` *Not recorded* is a statement about the record, not the person).
  This is an additive REDCap dropdown change for RareLink's `SexAtBirth`, not a
  migration. For Vital Status the opted-out *reason* is not preserved by the
  migration; representing it belongs in the consent section (7.x), not in vital
  status — open for 2.2.0.

- **A `400` from BioPortal aborted the whole validation run.** `get_remote_label`
  treated only `404` as "not found", but the bare-identifier fallback used for
  SNOMEDCT, LOINC and ICD10CM is not a well-formed IRI and comes back `400`, so
  the first unresolvable code raised instead of being recorded.

- **`poetry install --with dev` failed in both workflows.** `dev` and `test` are
  extras, not groups, so `merge_and_validate` and the drift job died at the
  install step. Now `-E dev -E test`; the `tests` job gains `-E test`, without
  which `pytest` was never installed.

- **A placeholder version could overwrite a real one.** `rd-cdm-sync-versions`
  replaced Sequence Ontology `2.6` with the string `unknown`, which no later run
  could undo. Placeholder versions are now reported and skipped. `SO` and `HGNC`
  are restored to their pre-sync values.

- **Version and label lookups used different BioPortal submissions.** `HGNC`
  labels resolve against `HGNC-NR` while the version was read from `HGNC`. Both
  now go through `validation_utils.BIOPORTAL_ACRONYM`, so the recorded version is
  the version of the submission the labels were checked against.

- **`VS X: missing member Y` was misleading.** The message described a live
  BioPortal resolution failure but read as a value-set membership failure. It is
  now `VS X: unresolvable code Y (no prefLabel in BioPortal …)`, and names
  `status: inactive` plus a successor as the remedy where that is the right
  answer.

- **`rd-cdm-validate` was never executed by any workflow.** `ci.yml` ran merge,
  class generation and `linkml validate`, but not the BioPortal check — so
  version and label drift had gone undetected despite the schedule and the
  configured API key.

- **`get_model_version()` was broken**: it called an undefined
  `_read_project_version` and looked for `pyproject.toml` inside `src/`. It now
  reads the version from `schema/rd_cdm.yaml`, the model's actual source of
  truth (as `rd-cdm-merge` already treated it).

### Changed

- **Ontology labels adopted from BioPortal** for the 20 codes whose recorded
  label had drifted from the terminology. Karyotypic Sex (9 codes, e.g.
  `734875008` `XX` → `Karyotype 46, XX`), Gender Identity (2), Vital Status (2),
  Age at Onset and Age at Diagnosis (`118189007` `Prenatal` → `Prenatal
  finding`), and Reference Genome (5, e.g. `LA26806-2` `GRCh38 (hg38)` →
  `GRCh38`). Every replaced string is preserved as `displayLabel`, so nothing
  curated is lost.

  ⚠️ RareLink copies these labels by hand into
  `rarelink_cdm/schema_definitions/*.yaml` and
  `rarelink_cdm/mappings/phenopackets/label_dicts.py`, and they surface as
  Phenopacket labels. Adopting them there is a separate change and will require
  re-baselining RareLink's golden files. Prefer `displayLabel` for REDCap
  dropdowns and other data-entry surfaces.

- **One source of truth for the model version.** `schema/rd_cdm.yaml` declares it;
  `rd-cdm-merge` propagates it into `instances/rd_cdm.yaml` and the generated
  JSON and CSV exports. `pyproject.toml` still carries its own copy because
  packaging requires it, but `tests/test_version_consistency.py` now fails if the
  two disagree, or if the merged instance is stale relative to the schema.

---

## v2.0.3

Initial published release of the RD-CDM package.
