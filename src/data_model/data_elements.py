from dataclasses import dataclass, field
from typing import List, Union, Optional
from .base_types import CodeSystem, Coding  # Assuming CodeSystem and Coding are in base_types
from .value_set import ValueSet

@dataclass(frozen=True, slots=True)
class DataElement:
    """Data class representing a data element in the RD CDM model."""
    ordinal: str
    section: str
    elementName: str
    elementCode: Coding  # Code will be part of the Coding data type
    elementCodeSystem: CodeSystem
    dataType: str
    dataSpecification: List[str]
    valueSet: Optional[ValueSet] = None  # ValueSet is optional
    fhirExpression_v4_0_1: Optional[str] = None
    recommendedVS_fhir: Optional[str] = None
    phenopacketSchemaElement_v2_0: Optional[str] = None
    recommendedVS_phenopacket: Optional[str] = None
    description: str = ""

@dataclass(slots=True, frozen=True)
class DataElementModel:
    """Data class representing a collection of data elements in the model."""
    dataElements: List[DataElement] = field(default_factory=list)
