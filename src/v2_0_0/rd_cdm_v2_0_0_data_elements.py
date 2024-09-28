from src.data_model.data_elements import DataElement
from src.data_model.value_set import ValueSet
from src.data_model.base_types import CodeSystem, Coding, Date, Code, Address

SNOMED = CodeSystem(name="SNOMED CT", namespace_prefix="SNOMED", url="https://www.snomed.org/snomed-ct")

class DATA_ELEMENTS_VERSIONS_V2_0_0:
    """Data elements definitions for version 2_0_0."""

    data_elements = [
        DataElement(
            ordinal="1.1",
            section="1. Formal Criteria",
            elementName="Pseudonym",
            elementCode=Coding(system=SNOMED, code="422549004"),
            elementCodeSystem=SNOMED,
            dataType="Identifier",
            dataSpecification=["n/a"],
            valueSet=None,
            fhirExpression_v4_0_1="Patient.identifier.value",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="Individual.id",
            recommendedDataSpec_phenopackets="None",
            description="The (local) patient-related identification code."
        ),
        DataElement(
            ordinal="1.2",
            section="1. Formal Criteria",
            elementName="Date of Admission",
            elementCode=Coding(system=SNOMED, code="399423000"),
            elementCodeSystem=SNOMED,
            dataType=Date,
            dataSpecification=["YYYY-MM-DD", "ISO 8601"],
            valueSet=None,
            fhirExpression_v4_0_1="Encounter.period.start",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="Individual.time_at_last_encounter",
            recommendedDataSpec_phenopackets="n/a",
            description="The date of admission or data capture of the individual."
        ),
        DataElement(
            ordinal="2.1",
            section="2. Personal Information",
            elementName="Date of Birth",
            elementCode=Coding(system=SNOMED, code="184099003"),
            elementCodeSystem=SNOMED,
            dataType=Date,
            dataSpecification=["YYYY", "YYYY-MM", "YYYY-MM-DD"],
            valueSet=None,
            fhirExpression_v4_0_1="Patient.birthDate",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="Individual.date_of_birth",
            recommendedDataSpec_phenopackets="n/a",
            description="The individual's date of birth."
        ),
        DataElement(
            ordinal="2.2",
            section="2. Personal Information",
            elementName="Sex at Birth",
            elementCode=Coding(system=SNOMED, code="281053000"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe / VSc"],
            valueSet=ValueSet(
                valueSetName="Sex at Birth Value Set v2.0.0",
                valueSetOrigin="RD CDM v2.0.0",
                valueSetLink="https://github.com/BIH-CEI/rd-cdm",
                display="Sex at Birth",
                valueSetCode=Coding(system=SNOMED, code="281053000"),
                valueSetCodeSystem=SNOMED,
                valueSetChoices=[]  # Add the choices if required
            ),
            fhirExpression_v4_0_1="Patient.extension:individual-recordedSexOrGender",
            recommendedDataSpec_fhir="Recorded Sex Or Gender Type",
            phenopacketSchemaElement_v2_0="Individual.sex",
            recommendedDataSpec_phenopackets="Sex",
            description="The individual's sex that was assigned at birth."
        ),
        DataElement(
            ordinal="2.3",
            section="2. Personal Information",
            elementName="Karyotypic Sex",
            elementCode=Coding(system=SNOMED, code="1296886006"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSc"],
            valueSet=ValueSet(
                valueSetName="Karyotypic Sex Value Set v2.0.0",
                valueSetOrigin="RD CDM v2.0.0",
                valueSetLink="https://github.com/your_repo_path/v2.0.0/value_sets_v2.0.0.json",
                display="Karyotypic Sex",
                valueSetCode=Coding(system=SNOMED, code="1296886006"),
                valueSetCodeSystem=SNOMED,
                valueSetChoices=[]
            ), 
            fhirExpression_v4_0_1="Observation.value",
            recommendedDataSpec_fhir="n/a",
            phenopacketSchemaElement_v2_0="Individual.karyotypic_sex",
            recommendedDataSpec_phenopackets="Karyotypic Sex",
            description="The chromosomal sex of an individual."
        ),
        DataElement(
            ordinal="2.4",
            section="2. Personal Information",
            elementName="Gender Identity",
            elementCode=Coding(system=SNOMED, code="263495000"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VSe / VSc"],
            valueSet=ValueSet(
                valueSetName="Gender Identity Value Set v2.0.0",
                valueSetOrigin="RD CDM v2.0.0",
                valueSetLink="https://github.com/your_repo_path/v2.0.0/value_sets_v2.0.0.json",
                display="Gender Identity",
                valueSetCode=Coding(system=SNOMED, code="263495000"),
                valueSetCodeSystem=SNOMED,
                valueSetChoices=[]
            ),  
            fhirExpression_v4_0_1="Patient.extension:individual-genderIdentity",
            recommendedDataSpec_fhir="Gender Identity",
            phenopacketSchemaElement_v2_0="Individual.gender",
            recommendedDataSpec_phenopackets="OntologyClass",
            description="The self-assigned gender of the individual."
        ),
        DataElement(
            ordinal="2.5",
            section="2. Personal Information",
            elementName="Country of Birth",
            elementCode=Coding(system=SNOMED, code="370159000"),
            elementCodeSystem=SNOMED,
            dataType=Code,
            dataSpecification=["VS"],  # Add relevant value set
            valueSet=None,  # Add relevant value set in the future
            fhirExpression_v4_0_1="Patient.extension:patient-birthPlace",
            recommendedDataSpec_fhir="Address",
            phenopacketSchemaElement_v2_0="n/a",
            recommendedDataSpec_phenopackets="n/a",
            description="The individual's country of birth."
        )
    ]
