from src.data_model.value_set import ValueSet, ValueSetChoice
from src.data_model.base_types import CodeSystem, Coding

# Example CodeSystem definitions
SNOMED_CT = CodeSystem(name="SNOMED CT", namespace_prefix="SNOMED", url="https://www.snomed.org/snomed-ct")

# Define the value sets for v2_0_0
class VALUE_SETS_VERSIONS_V2_0_0:
    """Value set definitions for version 2_0_0."""
    
    value_sets = [
        ValueSet(
            valueSetName="Sex at Birth Value Set v2.0.0",
            valueSetOrigin="RD CDM v2.0.0",
            valueSetLink="https://github.com/your_repo_path/v2.0.0/value_sets_v2.0.0.json",
            display="Sex at Birth",
            valueSetCode=Coding(system=SNOMED_CT, code="281053000"),
            valueSetCodeSystem=SNOMED_CT,
            valueSetChoices=[
                ValueSetChoice(
                    choiceDisplay="Female",
                    choiceCode=Coding(system=SNOMED_CT, code="248152002"),
                    choiceCodeSystem=SNOMED_CT
                ),
                ValueSetChoice(
                    choiceDisplay="Male",
                    choiceCode=Coding(system=SNOMED_CT, code="248153007"),
                    choiceCodeSystem=SNOMED_CT
                ),
                ValueSetChoice(
                    choiceDisplay="Patient sex unknown",
                    choiceCode=Coding(system=SNOMED_CT, code="184115007"),
                    choiceCodeSystem=SNOMED_CT
                ),
                ValueSetChoice(
                    choiceDisplay="Intersex",
                    choiceCode=Coding(system=SNOMED_CT, code="32570691000036108"),
                    choiceCodeSystem=SNOMED_CT
                ),
                ValueSetChoice(
                    choiceDisplay="Not recorded",
                    choiceCode=Coding(system=SNOMED_CT, code="1220561009"),
                    choiceCodeSystem=SNOMED_CT
                )
            ]
        )
    ]
