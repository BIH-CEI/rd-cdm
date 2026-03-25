.. _resources_file:

Resources
=========

.. tip::
    The RD-CDM paper has been published in *Nature Scientific Data*. 
    Read it `here <https://www.nature.com/articles/s41597-025-04558-z>`_.

All resources below always reflect the **latest released version** of the
RD-CDM. The version is embedded in every file as ``rd_cdm_version`` and
``rd_cdm_date`` — no need to check the filename.

To access a specific older version, install the corresponding PyPI release
(``pip install rd-cdm==2.0.2``) or browse the
`GitHub tags <https://github.com/BIH-CEI/rd-cdm/tags>`_.

------------------------------------------------------------------------

Schema
------

The LinkML schema is the single source of truth for the data model structure
and version:

- :download:`RD-CDM LinkML schema <../../src/rd_cdm/schema/rd_cdm.yaml>`

See `LinkML <https://linkml.io/linkml/>`_ for documentation on how to use it.

------------------------------------------------------------------------

Latest RD-CDM — Combined Files
--------------------------------

The merged instance file contains all code systems, data elements, and value
sets in a single file, stamped with ``rd_cdm_version`` and ``rd_cdm_date``:

- :download:`RD-CDM merged YAML <../../src/rd_cdm/instances/rd_cdm.yaml>`
- :download:`RD-CDM combined JSON <../../src/rd_cdm/instances/jsons/rd_cdm.json>`
- :download:`RD-CDM combined CSV <../../src/rd_cdm/instances/csvs/rd_cdm.csv>`

Download all files as a ZIP archive from GitHub:

- `Download latest release as ZIP <https://github.com/BIH-CEI/rd-cdm/archive/refs/heads/main.zip>`_
- `Browse all tagged releases <https://github.com/BIH-CEI/rd-cdm/releases>`_

------------------------------------------------------------------------

Latest RD-CDM — Individual Components
---------------------------------------

Code Systems
~~~~~~~~~~~~

- :download:`Code Systems YAML <../../src/rd_cdm/instances/code_systems.yaml>`
- :download:`Code Systems JSON <../../src/rd_cdm/instances/jsons/code_systems.json>`
- :download:`Code Systems CSV <../../src/rd_cdm/instances/csvs/code_systems.csv>`

Data Elements
~~~~~~~~~~~~~

- :download:`Data Elements YAML <../../src/rd_cdm/instances/data_elements.yaml>`
- :download:`Data Elements JSON <../../src/rd_cdm/instances/jsons/data_elements.json>`
- :download:`Data Elements CSV <../../src/rd_cdm/instances/csvs/data_elements.csv>`

Value Sets
~~~~~~~~~~

- :download:`Value Sets YAML <../../src/rd_cdm/instances/value_sets.yaml>`
- :download:`Value Sets JSON <../../src/rd_cdm/instances/jsons/value_sets.json>`
- :download:`Value Sets CSV <../../src/rd_cdm/instances/csvs/value_sets.csv>`

------------------------------------------------------------------------

RD-CDM v2.0.0 (outdated)
--------------------------

The original v2.0.0 release is available on
`Figshare <https://figshare.com/articles/dataset/_b_Common_Data_Model_for_Rare_Diseases_b_based_on_the_ERDRI-CDS_HL7_FHIR_and_the_GA4GH_Phenopackets_Schema_v2_0_/26509150>`_
and as a
`GitHub release <https://github.com/BIH-CEI/rd-cdm/releases/tag/v2.0.0>`_.

Excel Table
~~~~~~~~~~~

- :download:`RD-CDM v2.0.0 Excel Table <../_static/v2_0_0/RD-CDM v2.0.0.xlsx>`

JSON Files
~~~~~~~~~~

- :download:`Entire RD-CDM v2.0.0 JSON <../../res/v2_0_0/rd_cdm_v2_0_0.json>`
- :download:`Code Systems v2.0.0 JSON <../../res/v2_0_0/rd_cdm_codesystems_v2_0_0.json>`
- :download:`Data Elements v2.0.0 JSON <../../res/v2_0_0/rd_cdm_data_elements_v2_0_0.json>`
- :download:`Value Sets v2.0.0 JSON <../../res/v2_0_0/rd_cdm_value_sets_v2_0_0.json>`

CSV Files
~~~~~~~~~

- :download:`Combined RD-CDM v2.0.0 CSV <../../res/v2_0_0/rd_cdm_v2_0_0.csv>`
- :download:`Code Systems v2.0.0 CSV <../../res/v2_0_0/rd_cdm_codesystems_v2_0_0.csv>`
- :download:`Data Elements v2.0.0 CSV <../../res/v2_0_0/rd_cdm_data_elements_v2_0_0.csv>`
- :download:`Value Sets v2.0.0 CSV <../../res/v2_0_0/rd_cdm_value_sets_v2_0_0.csv>`

For additional details see :ref:`background_file`.