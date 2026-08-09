# Contributing

As we are actively developing the RD-CDM, we welcome contributions in the form
of new resources, new concepts, or new relationships. This RD-CDM is a
non-balloted extension of the ERDRI-CDS which aims to provide an
internationally viable template for the development of country-specific common
data models. Furthermore, the RD-CDM is designed to be compatible with the GA4GH
Phenopacket Schema, HL7 FHIR, and the International Patient Summary.

We encourage contributions to the RD-CDM. These contributions can be in the form
of new resources, new concepts, relationships, or implementations.

!!! tip
    The RD-CDM paper has now been published at Nature Scientific Data. You can
    read it [here](https://www.nature.com/articles/s41597-025-04558-z)!

If you would like to contribute, please consider the following:

## 1. GitHub Issues

Feel free to create a new issue on our
[GitHub repository](https://github.com/BIH-CEI/rd-cdm/issues). We welcome
feedback, suggestions, and bug reports.

## 2. Reach out directly

If you have any questions or suggestions, please feel free to reach out to us.
You can contact us via email at <adam.graefe@charite.de>.

## 3. Implementation

We actively encourage users to implement and test our RD-CDM in various
healthcare information systems. If you have implemented the RD-CDM in your
system, please let us know. We would be happy to hear about your experience and
any feedback you may have.

!!! note
    RareLink is our implementation of the RD-CDM in REDCap, enabling the
    generation of FHIR resources and Phenopackets from REDCap. If you would like
    to contribute to the implementation or have any questions, feel free to
    reach out or find us on [GitHub](https://github.com/BIH-CEI/rarelink).

## 4. Documentation

If you would like to contribute to the documentation, please feel free to create
an issue in our [GitHub repository](https://github.com/BIH-CEI/rd-cdm/issues) or
reach out to us directly. We are always looking for ways to improve our
documentation and welcome any suggestions.

## Working on the model

`main` is the only long-lived branch. Branch from it, open a pull request
against it, and let CI run.

```bash
git clone https://github.com/BIH-CEI/rd-cdm.git
cd rd-cdm
poetry install -E dev -E test
poetry run pytest -q
```

After editing anything under `src/rd_cdm/instances/`:

```bash
poetry run rd-cdm-merge
poetry run rd-cdm-validate --offline    # structural checks, no API key needed
poetry run rd-cdm-profile
poetry run rd-cdm-json && poetry run rd-cdm-csv
poetry run rd-cdm-docs
```

The generated artefacts are committed, and CI fails if they are stale relative
to their sources — so run the sequence above and commit the result with your
change.

Some conventions worth knowing:

- **The LinkML schema owns the version.** `schema/rd_cdm.yaml` declares it;
  `rd-cdm-merge` propagates it everywhere else, and `pyproject.toml` carries a
  copy only because packaging requires one. A test fails if they disagree.
- **A value set's `id` is the CURIE of the data element it constrains.** Data
  elements reference value sets by *label*, so labels must be unique too. Both
  are enforced by `rd-cdm-validate --offline`.
- **BioPortal is the terminology authority.** A code that does not resolve there
  is marked `status: inactive` with a `replacedBy` and withdrawn from new
  capture, rather than deleted — records already captured against it must stay
  interpretable.
