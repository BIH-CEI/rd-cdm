from src.data_model.value_set import ValueSet, ValueSetChoice
from src.data_model.base_types import CodeSystem, Coding
from src.data_model.codesystems import CodeSystems

SNOMED = CodeSystems.SNOMED
HL7FHIR = CodeSystems.HL7FHIR

class VALUE_SETS_VERSIONS_V2_0_0:
    """Value set definitions for version 2_0_0."""
    
    value_sets = [
        ValueSet(
            valueSetName="Sex at Birth Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/your_repo_path/v2.0.0/value_sets_v2.0.0.json",
            display="Sex at Birth",
            valueSetCode=Coding(system=SNOMED, code="281053000"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Female",
                    choiceCode=Coding(system=SNOMED, code="248152002"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Male",
                    choiceCode=Coding(system=SNOMED, code="248153007"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Patient sex unknown",
                    choiceCode=Coding(system=SNOMED, code="184115007"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Intersex",
                    choiceCode=Coding(system=SNOMED, code="32570691000036108"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Not recorded",
                    choiceCode=Coding(system=SNOMED, code="1220561009"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Karyotypic Sex Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/your_repo_path/v2.0.0/value_sets_v2.0.0.json",
            display="Karyotypic Sex",
            valueSetCode=Coding(system=SNOMED, code="1296886006"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="XX",
                    choiceCode=Coding(system=SNOMED, code="734875008"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XY",
                    choiceCode=Coding(system=SNOMED, code="734876009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="X0",
                    choiceCode=Coding(system=SNOMED, code="80427008"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XXY",
                    choiceCode=Coding(system=SNOMED, code="65162001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XXX",
                    choiceCode=Coding(system=SNOMED, code="35111009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XXYY",
                    choiceCode=Coding(system=SNOMED, code="403760006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XXXY",
                    choiceCode=Coding(system=SNOMED, code="78317008"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XXXX",
                    choiceCode=Coding(system=SNOMED, code="10567003"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="XYY",
                    choiceCode=Coding(system=SNOMED, code="48930007"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Other",
                    choiceCode=Coding(system=SNOMED, code="74964007"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Gender Identity Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/your_repo_path/v2.0.0/value_sets_v2.0.0.json",
            display="Gender Identity",
            valueSetCode=Coding(system=SNOMED, code="263495000"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Female gender identity",
                    choiceCode=Coding(system=SNOMED, code="446141000124107"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Male gender identity",
                    choiceCode=Coding(system=SNOMED, code="446151000124109"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Gender unknown",
                    choiceCode=Coding(system=SNOMED, code="394743007"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Identifies as nonbinary gender",
                    choiceCode=Coding(system=SNOMED, code="33791000087105"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Not recorded",
                    choiceCode=Coding(system=SNOMED, code="1220561009"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Vital Status Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/your_repo_path/v2.0.0/value_sets_v2.0.0.json",
            display="Vital Status",
            valueSetCode=Coding(system=SNOMED, code="278844005"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Alive",
                    choiceCode=Coding(system=SNOMED, code="438949009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Dead",
                    choiceCode=Coding(system=SNOMED, code="419099009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown - Lost in follow-up",
                    choiceCode=Coding(system=SNOMED, code="399307001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown - Opted-out",
                    choiceCode=Coding(system=SNOMED, code="185924006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown - Other Reason",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Age Category Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/your_repo_path/v2.0.0/value_sets_v2.0.0.json",
            display="Age Category",
            valueSetCode=Coding(system=SNOMED, code="105727008"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Infancy",
                    choiceCode=Coding(system=SNOMED, code="3658006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Toddler",
                    choiceCode=Coding(system=SNOMED, code="713153009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Childhood",
                    choiceCode=Coding(system=SNOMED, code="255398004"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Adolescence",
                    choiceCode=Coding(system=SNOMED, code="263659003"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Adulthood",
                    choiceCode=Coding(system=SNOMED, code="41847000"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Fetal period",
                    choiceCode=Coding(system=SNOMED, code="303112003"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Dead",
                    choiceCode=Coding(system=SNOMED, code="419099009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Vital Status Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/your_repo_path/v2.0.0/value_sets_v2.0.0.json",
            display="Vital Status",
            valueSetCode=Coding(system=SNOMED, code="278844005"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Alive",
                    choiceCode=Coding(system=SNOMED, code="438949009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Dead",
                    choiceCode=Coding(system=SNOMED, code="419099009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown - Lost in follow-up",
                    choiceCode=Coding(system=SNOMED, code="399307001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown - Opted-out",
                    choiceCode=Coding(system=SNOMED, code="185924006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown - Other Reason",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Age Category Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/your_repo_path/v2.0.0/value_sets_v2.0.0.json",
            display="Age Category",
            valueSetCode=Coding(system=SNOMED, code="105727008"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Infancy",
                    choiceCode=Coding(system=SNOMED, code="3658006"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Toddler",
                    choiceCode=Coding(system=SNOMED, code="713153009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Childhood",
                    choiceCode=Coding(system=SNOMED, code="255398004"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Adolescence",
                    choiceCode=Coding(system=SNOMED, code="263659003"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Adulthood",
                    choiceCode=Coding(system=SNOMED, code="41847000"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Fetal period",
                    choiceCode=Coding(system=SNOMED, code="303112003"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Dead",
                    choiceCode=Coding(system=SNOMED, code="419099009"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown",
                    choiceCode=Coding(system=SNOMED, code="261665006"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        ValueSet(
            valueSetName="Undiagnosed RD Case Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/your_repo_path/v2.0.0/value_sets_v2.0.0.json",
            display="Undiagnosed RD Case",
            valueSetCode=Coding(system=SNOMED, code="723663001"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Yes",
                    choiceCode=Coding(system=SNOMED, code="373066001"),
                    choiceCodeSystem=SNOMED
                ),
                ValueSetChoice(
                    choiceDisplay="No",
                    choiceCode=Coding(system=SNOMED, code="373067005"),
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
        # 4. Care Pathway
        ValueSet(
            valueSetName="Encounter Status Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/your_repo_path/v2.0.0/value_sets_v2.0.0.json",
            display="Encounter Status",
            valueSetCode=Coding(system=SNOMED, code="305058001"),
            valueSetCodeSystem=SNOMED,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Planned", 
                    choiceCode=Coding(system=HL7FHIR, code="planned"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Arrived", 
                    choiceCode=Coding(system=HL7FHIR, code="arrived"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Triaged", 
                    choiceCode=Coding(system=HL7FHIR, code="triaged"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="In Progress", 
                    choiceCode=Coding(system=HL7FHIR, code="in-progress"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="On Leave", 
                    choiceCode=Coding(system=HL7FHIR, code="onleave"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Finished", 
                    choiceCode=Coding(system=HL7FHIR, code="finished"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Cancelled", 
                    choiceCode=Coding(system=HL7FHIR, code="cancelled"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Entered in Error", 
                    choiceCode=Coding(system=HL7FHIR, code="entered-in-error"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown", 
                    choiceCode=Coding(system=HL7FHIR, code="unknown"), 
                    choiceCodeSystem=HL7FHIR
                )
            ]
        ),
        ValueSet(
            valueSetName="Encounter Class Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/your_repo_path/v2.0.0/value_sets_v2.0.0.json",
            display="Encounter Class",
            valueSetCode=Coding(system=HL7FHIR, code="encounter.class"),
            valueSetCodeSystem=[HL7FHIR, SNOMED],
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Ambulatory", 
                    choiceCode=Coding(system=HL7FHIR, code="AMB"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Inpatient", 
                    choiceCode=Coding(system=HL7FHIR, code="IMP"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Observation", 
                    choiceCode=Coding(system=HL7FHIR, code="OBSENC"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Emergency", 
                    choiceCode=Coding(system=HL7FHIR, code="EMER"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Virtual", 
                    choiceCode=Coding(system=HL7FHIR, code="VR"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Home Health", 
                    choiceCode=Coding(system=HL7FHIR, code="HH"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="RD Specialist Center", 
                    choiceCode=Coding(system=HL7FHIR, code="RDC"), 
                    choiceCodeSystem=HL7FHIR
                ),
                ValueSetChoice(
                    choiceDisplay="Unknown", 
                    choiceCode=Coding(system=SNOMED, code="261665006"), 
                    choiceCodeSystem=SNOMED
                )
            ]
        ),
    ]
    