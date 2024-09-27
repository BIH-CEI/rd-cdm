from dataclasses import dataclass, field
from typing import List, Union, Literal
from . import CodeSystem

@dataclass(frozen=True, slots=True, eq=True)
class Coding:
    """Data class for Coding

    A `Coding` is a representation of a concept defined by a code and a code system. It is used in the `CodeableConcept`
    data class.

    :ivar system: The code system that defines the code.
    :ivar code: The code that represents the concept (treated as 'Code').
    :ivar display: The human-readable representation of the concept.
    :ivar text: A human-readable description or additional text of the concept.
    """
    system: Union[str, CodeSystem] = field(compare=True)
    code: str = field(compare=True)  # Assuming "Code" is a string representation of the code.
    display: str = field(default="", compare=False)
    text: str = field(default="", compare=False)

    @staticmethod
    def parse_coding(
            coding_str: str,
            resources: List[CodeSystem],
            compliance: Literal['soft', 'hard'] = 'soft'
    ) -> 'Coding':
        """Parse a string representing a coding into a Coding object.

        Expected format: <namespace_prefix>:<code>.

        E.g.:
        >>> Coding.parse_coding("SNOMED:404684003", [code_system.SNOMED_CT])
        Coding(system=CodeSystem(name=SNOMED CT, name space prefix=SNOMED, version=0.0.0),
               code='404684003', display='', text='')

        This function recognizes name space prefixes belonging to code systems provided in the resources list.
        If a name space is not found, it returns a Coding object with the system as the name space prefix and the code.

        :param coding_str: A string representing a coding.
        :param resources: A list of all resources (code systems) used.
        :param compliance: Whether to throw a ValueError or just issue a warning if a name space prefix is not found.
        :return: A Coding object as specified in the input string.
        """
        try:
            namespace, code = coding_str.split(":")
        except ValueError:
            raise ValueError(f"Invalid coding format: {coding_str}. Expected format: <namespace_prefix>:<code>")

        for resource in resources:
            if resource.namespace_prefix == namespace:
                return Coding(system=resource, code=code)

        if compliance == 'hard':
            raise ValueError(f"Code system with namespace prefix '{namespace}' not found in resources.")
        else:
            print(f"Warning: Code system with namespace prefix '{namespace}' not found in resources.")
            print(f"Warning: Returning Coding object with system as namespace prefix and code as '{code}'")
            return Coding(system=namespace, code=code)

    def __str__(self):
        if isinstance(self.system, CodeSystem):
            return f"{self.system.namespace_prefix}:{self.code}"
        return f"{self.system}:{self.code}"


@dataclass(frozen=True, slots=True, eq=True)
class CodeableConcept:
    """Data class for CodeableConcept

    A `CodeableConcept` represents a concept defined by one or more codings. It may also have a text representation.

    :ivar coding: A list of `Coding` instances that define the concept.
    :ivar text: A text representation of the concept.
    """
    coding: List[Coding] = field(compare=True)
    text: str = field(default="", compare=False)

    def __str__(self):
        return f"CodeableConcept(codings=[{', '.join(map(str, self.coding))}], text={self.text})"
