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


v2.0.3 (2026-03-24)
--------------------

Code System Version Updates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All ontology and code system versions have been updated to their latest
releases as reported by BioPortal. The following version drifts were
resolved:

.. list-table::
   :header-rows: 1
   :widths: 20 30 30

   * - Code System
     - Previous Version
     - Updated Version
   * - SNOMEDCT
     - SNOMEDCT_US_2024_09_01
     - 2025AB
   * - LOINC
     - LNC278
     - 281
   * - HP
     - 2025-05-06
     - 2026-02-16
   * - NCIT
     - 24.01e
     - 26.02d
   * - NCBITAXON
     - NCBI2024_04_02
     - 2025_04_10
   * - GENO
     - 2023-10-08
     - 2026-02-02
   * - UO
     - 2023-05-25
     - 2026-01-16
   * - ECO
     - 2025-06-23
     - releases/2025-06-23
   * - ICD10CM
     - ICD10CM_2025
     - 2026
   * - MONDO
     - 2025-06-03
     - 2026-03-03
   * - ORDO
     - 4.7
     - 4.8

Data Element Update: Sex at Birth (2.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The code for data element **2.2 Sex at Birth** has been updated. The
previous SNOMED CT concept ``281053000 | Sex of baby at delivery
(observable entity)`` was identified as inactive (deprecated) in the
SNOMED CT browser.

The element is now coded using the LOINC concept:

- **LOINC 76689-9** — *Sex assigned at birth*

This aligns with HL7 FHIR's ``Patient`` resource and is semantically
precise as a question/observable code. The value set choices (Female,
Male, Unknown, etc.) remain SNOMED CT encoded as before.

Repository and Package Structure Refactor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The versioned folder structure inside ``src/rd_cdm/instances/`` has been
removed. Previously, each data model version occupied a dedicated
subdirectory (e.g., ``instances/v2_0_2/``) with the version repeated in
filenames (e.g., ``rd_cdm_v2_0_2.yaml``). This created redundancy since
Git tags and PyPI versioning already serve as the version archive.

**New structure:**

.. code-block:: text

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

**Version is now embedded in every exported file.** The fields
``rd_cdm_version`` and ``rd_cdm_date`` are defined in the LinkML schema
(``schema/rd_cdm.yaml``) and written into every merged and exported file
by ``rd-cdm-merge``. Every standalone YAML, JSON, or CSV file is
therefore self-describing.

To use an older version of the model, use the corresponding Git tag or
pin the PyPI package:

.. code-block:: bash

   pip install rd-cdm==2.0.2

CLI Naming Update
~~~~~~~~~~~~~~~~~

All CLI commands have been renamed from ``rdcdm-*`` to ``rd-cdm-*`` for
consistency with the PyPI package name ``rd-cdm``:

.. list-table::
   :header-rows: 1
   :widths: 40 40

   * - Old command
     - New command
   * - ``rdcdm-merge``
     - ``rd-cdm-merge``
   * - ``rdcdm-json``
     - ``rd-cdm-json``
   * - ``rdcdm-csv``
     - ``rd-cdm-csv``
   * - ``rdcdm-validate``
     - ``rd-cdm-validate``

The ``--version`` / ``-v`` argument has been removed from all CLI tools
since version resolution via subdirectories is no longer needed.

The recommended workflow after updating instance files is:

.. code-block:: bash

   rd-cdm-merge && rd-cdm-json && rd-cdm-csv && rd-cdm-validate

Validation Improvements
~~~~~~~~~~~~~~~~~~~~~~~~

The ``rd-cdm-validate`` command now shows progress bars (via ``tqdm``)
for each of the three validation phases: code system version checking,
data element validation, and value set code validation. The current
element being checked is shown in the progress bar postfix.

The validation summary now reports the data model version at the top:

.. code-block:: text

   === RD-CDM VALIDATION SUMMARY (model version: 2.0.3) ===

Dependency Changes
~~~~~~~~~~~~~~~~~~

The following dependencies were removed as they were not used by the
package:

- ``numpy``
- ``requests-cache``
- ``jsonschema``
- ``oaklib``

``linkml`` has been moved from a core runtime dependency to an optional
``dev`` extra, since it is only needed to regenerate the Python classes
from the schema. Users installing ``rd-cdm`` for data access do not
require it:

.. code-block:: bash

   pip install rd-cdm        # no linkml
   pip install rd-cdm[dev]   # includes linkml for schema development

``tqdm`` has been added as a core dependency for validation progress
reporting.

Python Class Generation
~~~~~~~~~~~~~~~~~~~~~~~~

The ``gen_pydantic.py`` utility now generates both output files from the
schema in a single run:

- ``src/rd_cdm/python_classes/rd_cdm.py`` — LinkML runtime dataclasses
  (via ``PythonGenerator``)
- ``src/rd_cdm/python_classes/rd_cdm_pydantic.py`` — Pydantic v2 models
  (via ``PydanticGenerator``)

Custom top-level schema fields (``date``) that are not valid
``SchemaDefinition`` fields are stripped into a temporary file before
generation to avoid ``SchemaDefinition.__init__()`` errors.


v2.0.1 & v2.0.2 (2025-08-07)
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


v2.0.0 (2025-02-08)
----------------------------

The RD-CDM has been updated to version 2.0.0 as the corresponding
manuscript was published.


v2.0.0.dev0 (2024-09-30)
-------------------------------

- Initial release of the RD-CDM in development and review. 
