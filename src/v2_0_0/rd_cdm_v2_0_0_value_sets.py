from src.data_model.value_set import ValueSet, ValueSetChoice
from src.data_model.base_types import CodeSystem, Coding

# Example CodeSystem definitions
SNOMED = CodeSystem(name="SNOMED CT", namespace_prefix="SNOMED", url="https://www.snomed.org/snomed-ct")

# Define the value sets for v2_0_0
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
        )
    ]