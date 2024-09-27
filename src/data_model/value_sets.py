from dataclasses import dataclass, field
from typing import List
from . import Code, CodableConcept

@dataclass(slots=True, frozen=True)
class ValueSetChoice:
    """Data class representing a single choice in a value set."""
    choiceDisplay: str
    choiceCode: Code
    choiceCodeSystem: str

@dataclass(slots=True, frozen=True)
class ValueSet:
    """Data class representing a value set."""
    valueSetName: str
    valueSetOrigin: str
    valueSetLink: str
    display: str
    valueSetCode: Code
    valueSetCodeSystem: str
    valueSetChoices: List[ValueSetChoice] = field(default_factory=list)


