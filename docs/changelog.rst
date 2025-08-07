.. _changelog: 

Changelog
================

.. tip::
    The RD-CDM paper has now been published at Nature Scientific Data. You can 
    read it `here <https://www.nature.com/articles/s41597-025-04558-z>`_!

This changelog provides a history of the changes to the RD-CDM.

.. note:: 
    Previous versions (v1.0 - v1.7) were developed in a German context and are
    not publicly available.


Version 2.0.1 (2025-08-07)
--------------------------

**What’s new**

- **Complete LinkML model definition** polished and consolidated for RD-CDM v2.0.1.
  - `Coding`, `ValueSet`, `DataElement`, and `CodeSystem` clarified and aligned.
  - `elementCode.system` and `CodeSystem.id` now consistently use ontology acronyms (e.g., ``SNOMEDCT``, ``LOINC``, ``HP``, ``NCIT``).

- **Automated validation against BioPortal (new CLI: ``rd-cdm-validate``)**.
  - Validates all **DataElement.elementCode** and **ValueSet.codes** entries against the **latest** BioPortal content.
  - Summarizes results: number of data elements & value set members checked, valid/missing/skipped terms, label-drift warnings.
  - **Label drift** (model label ≠ live ``prefLabel``) is reported as a **warning**, not a failure.
  - **Composite SNOMED expressions** (codes containing ``=``) are **skipped** on purpose.
  - Handles LOINC part/answer codes (e.g., ``LA26406-1``) and NCIt IRIs via the EVS Thesaurus mapping.
  - Uses an explicit ontology mapping (HP/MONDO/OBO, NCIT/EVS, SNOMEDCT, LOINC, etc.) + CURIE and IRI fallbacks.

- **Version checks (live vs. model)**
  - By default checks every ``CodeSystem`` in the instance directory against BioPortal’s **latest_submission**.
  - A configurable **skip list** excludes non-ontology systems (e.g., ``CustomCode``, ``GA4GH``, ``HL7FHIR``) from version drift checks.
  - Environment variable: ``BIOPORTAL_API_KEY`` is required.

- **Dynamic instance version resolution**
  - Validation and merge tooling now auto-locate the latest instances directory:
    - ``src/rd_cdm/instances/{version}/rd_cdm_full.yaml`` is chosen from ``--version``, then ``pyproject.toml`` (``tool.poetry.version``), then the newest folder on disk.
  - Works across future releases without changing hard-coded paths.

- **Merge improvements**
  - ``merge_instances.py`` updated to reliably rebuild ``rd_cdm_full.yaml`` from ``code_systems.yaml``, ``data_elements.yaml``, and ``value_sets.yaml`` in the resolved version directory.

- **Export utilities**
  - Added helpers to export LinkML instances to **JSON** and **CSV** for downstream processing (via LinkML dumpers), improving round-tripping and interoperability.

**Data & label consistency updates**

- Adjusted several labels to match BioPortal ``prefLabel`` (reported previously as label drift), e.g.:
  - SNOMED CT: ``410605003`` → “Confirmed present” (capitalization).
  - HPO onset labels simplified to BioPortal’s canonical forms (e.g., “Embryonal onset”).
- Ensured validation uses **ValueSet.codes** (the members) rather than the ValueSet ``id`` itself.

**CodeSystem version alignment**

- Code system versions in the schema updated to BioPortal’s current **latest_submission**:
  - **HP** → ``hp/releases/2025-05-06``
  - **SNOMEDCT** → ``SNOMEDCT_US_2024_09_01``
  - **LOINC** → ``LNC278``
  - **NCIT** → ``24.01e``

  (Version drift is now reported as a **warning** during validation.)

**Breaking/behavioral notes**

- ``elementCode.system`` must match a ``CodeSystem.id`` (e.g., ``SNOMEDCT``, ``LOINC``).
- Validation of SNOMED CT **post-coordination** / ECL (codes containing ``=``) is **skipped**.
- Version checks intentionally **exclude** systems in the skip list (configurable).

**How to run**

.. code-block:: bash

    export BIOPORTAL_API_KEY=...   # required for live checks
    rd-cdm-validate                # validates the resolved instance version

    # Optional: validate a specific instance version folder
    rd-cdm-validate --version 2.0.1


Version 2.0.0 (2025-02-08)
----------------------------

The RD-CDM has been updated to version 2.0.0 as the corresponding
manuscript was published.


Version 2.0.0.dev0 (2024-09-30)
-------------------------------

- Initial release of the RD-CDM in development and review. 
