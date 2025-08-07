# Auto generated from rd_cdm.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-08-07T14:59:42
# Schema: rd_cdm.schema.yaml
#
# id: https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml
# description:
# license: CC0


from dataclasses import dataclass
from typing import (
    Any,
    ClassVar,
    Optional,
    Union
)

from jsonasobj2 import (
    as_dict
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.metamodelcore import (
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_str
)
from rdflib import (
    URIRef
)

from linkml_runtime.linkml_model.types import Curie
from linkml_runtime.utils.metamodelcore import URI

metamodel_version = "1.7.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDCDM = CurieNamespace('rdcdm', 'https://github.com/BIH-CEI/rd-cdm/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/')


# Types

# Class references
class CodeSystemId(extended_str):
    pass


@dataclass(repr=False)
class RdCdm(YAMLRoot):
    """
    Root class for the Rare Disease Common Data Model (RD-CDM)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDCDM["linkml/rd_cdm.schema.yaml/RdCdm"]
    class_class_curie: ClassVar[str] = "rdcdm:linkml/rd_cdm.schema.yaml/RdCdm"
    class_name: ClassVar[str] = "RdCdm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/RdCdm")

    code_systems: Optional[Union[dict[Union[str, CodeSystemId], Union[dict, "CodeSystem"]], list[Union[dict, "CodeSystem"]]]] = empty_dict()
    data_elements: Optional[Union[Union[dict, "DataElement"], list[Union[dict, "DataElement"]]]] = empty_list()
    value_sets: Optional[Union[Union[dict, "ValueSet"], list[Union[dict, "ValueSet"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="code_systems", slot_type=CodeSystem, key_name="id", keyed=True)

        if not isinstance(self.data_elements, list):
            self.data_elements = [self.data_elements] if self.data_elements is not None else []
        self.data_elements = [v if isinstance(v, DataElement) else DataElement(**as_dict(v)) for v in self.data_elements]

        if not isinstance(self.value_sets, list):
            self.value_sets = [self.value_sets] if self.value_sets is not None else []
        self.value_sets = [v if isinstance(v, ValueSet) else ValueSet(**as_dict(v)) for v in self.value_sets]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CodeSystem(YAMLRoot):
    """
    Metadata for an ontology or code system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDCDM["linkml/rd_cdm.schema.yaml/CodeSystem"]
    class_class_curie: ClassVar[str] = "rdcdm:linkml/rd_cdm.schema.yaml/CodeSystem"
    class_name: ClassVar[str] = "CodeSystem"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/CodeSystem")

    id: Union[str, CodeSystemId] = None
    namespace_iri: Union[str, URI] = None
    version: str = None
    title: Optional[str] = None
    homepage: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CodeSystemId):
            self.id = CodeSystemId(self.id)

        if self._is_empty(self.namespace_iri):
            self.MissingRequiredField("namespace_iri")
        if not isinstance(self.namespace_iri, URI):
            self.namespace_iri = URI(self.namespace_iri)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.homepage is not None and not isinstance(self.homepage, URI):
            self.homepage = URI(self.homepage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Coding(YAMLRoot):
    """
    A code + code system reference
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDCDM["linkml/rd_cdm.schema.yaml/Coding"]
    class_class_curie: ClassVar[str] = "rdcdm:linkml/rd_cdm.schema.yaml/Coding"
    class_name: ClassVar[str] = "Coding"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/Coding")

    system: str = None
    code: str = None
    label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, str):
            self.system = str(self.system)

        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, str):
            self.code = str(self.code)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ValueSet(YAMLRoot):
    """
    A set of permitted codes for a data element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDCDM["linkml/rd_cdm.schema.yaml/ValueSet"]
    class_class_curie: ClassVar[str] = "rdcdm:linkml/rd_cdm.schema.yaml/ValueSet"
    class_name: ClassVar[str] = "ValueSet"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/ValueSet")

    id: Union[str, Curie] = None
    label: str = None
    codes: Optional[Union[Union[dict, Coding], list[Union[dict, Coding]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Curie):
            self.id = Curie(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        self._normalize_inlined_as_dict(slot_name="codes", slot_type=Coding, key_name="system", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataElement(YAMLRoot):
    """
    A single data field in the RD-CDM
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDCDM["linkml/rd_cdm.schema.yaml/DataElement"]
    class_class_curie: ClassVar[str] = "rdcdm:linkml/rd_cdm.schema.yaml/DataElement"
    class_name: ClassVar[str] = "DataElement"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/BIH-CEI/rd-cdm/linkml/rd_cdm.schema.yaml/DataElement")

    ordinal: str = None
    elementName: str = None
    elementCode: Union[dict, Coding] = None
    elementCodeSystem: str = None
    section: Optional[str] = None
    dataType: Optional[str] = None
    dataSpecification: Optional[Union[str, list[str]]] = empty_list()
    valueSet: Optional[str] = None
    fhirExpression_v4_0_1: Optional[str] = None
    recommendedDataSpec_fhir: Optional[str] = None
    phenopacketSchemaElement_v2_0: Optional[str] = None
    recommendedDataSpec_phenopackets: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ordinal):
            self.MissingRequiredField("ordinal")
        if not isinstance(self.ordinal, str):
            self.ordinal = str(self.ordinal)

        if self._is_empty(self.elementName):
            self.MissingRequiredField("elementName")
        if not isinstance(self.elementName, str):
            self.elementName = str(self.elementName)

        if self._is_empty(self.elementCode):
            self.MissingRequiredField("elementCode")
        if not isinstance(self.elementCode, Coding):
            self.elementCode = Coding(**as_dict(self.elementCode))

        if self._is_empty(self.elementCodeSystem):
            self.MissingRequiredField("elementCodeSystem")
        if not isinstance(self.elementCodeSystem, str):
            self.elementCodeSystem = str(self.elementCodeSystem)

        if self.section is not None and not isinstance(self.section, str):
            self.section = str(self.section)

        if self.dataType is not None and not isinstance(self.dataType, str):
            self.dataType = str(self.dataType)

        if not isinstance(self.dataSpecification, list):
            self.dataSpecification = [self.dataSpecification] if self.dataSpecification is not None else []
        self.dataSpecification = [v if isinstance(v, str) else str(v) for v in self.dataSpecification]

        if self.valueSet is not None and not isinstance(self.valueSet, str):
            self.valueSet = str(self.valueSet)

        if self.fhirExpression_v4_0_1 is not None and not isinstance(self.fhirExpression_v4_0_1, str):
            self.fhirExpression_v4_0_1 = str(self.fhirExpression_v4_0_1)

        if self.recommendedDataSpec_fhir is not None and not isinstance(self.recommendedDataSpec_fhir, str):
            self.recommendedDataSpec_fhir = str(self.recommendedDataSpec_fhir)

        if self.phenopacketSchemaElement_v2_0 is not None and not isinstance(self.phenopacketSchemaElement_v2_0, str):
            self.phenopacketSchemaElement_v2_0 = str(self.phenopacketSchemaElement_v2_0)

        if self.recommendedDataSpec_phenopackets is not None and not isinstance(self.recommendedDataSpec_phenopackets, str):
            self.recommendedDataSpec_phenopackets = str(self.recommendedDataSpec_phenopackets)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.rdCdm__code_systems = Slot(uri=DEFAULT_.code_systems, name="rdCdm__code_systems", curie=DEFAULT_.curie('code_systems'),
                   model_uri=DEFAULT_.rdCdm__code_systems, domain=None, range=Optional[Union[dict[Union[str, CodeSystemId], Union[dict, CodeSystem]], list[Union[dict, CodeSystem]]]])

slots.rdCdm__data_elements = Slot(uri=DEFAULT_.data_elements, name="rdCdm__data_elements", curie=DEFAULT_.curie('data_elements'),
                   model_uri=DEFAULT_.rdCdm__data_elements, domain=None, range=Optional[Union[Union[dict, DataElement], list[Union[dict, DataElement]]]])

slots.rdCdm__value_sets = Slot(uri=DEFAULT_.value_sets, name="rdCdm__value_sets", curie=DEFAULT_.curie('value_sets'),
                   model_uri=DEFAULT_.rdCdm__value_sets, domain=None, range=Optional[Union[Union[dict, ValueSet], list[Union[dict, ValueSet]]]])

slots.codeSystem__id = Slot(uri=DEFAULT_.id, name="codeSystem__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.codeSystem__id, domain=None, range=URIRef)

slots.codeSystem__namespace_iri = Slot(uri=DEFAULT_.namespace_iri, name="codeSystem__namespace_iri", curie=DEFAULT_.curie('namespace_iri'),
                   model_uri=DEFAULT_.codeSystem__namespace_iri, domain=None, range=Union[str, URI])

slots.codeSystem__version = Slot(uri=DEFAULT_.version, name="codeSystem__version", curie=DEFAULT_.curie('version'),
                   model_uri=DEFAULT_.codeSystem__version, domain=None, range=str)

slots.codeSystem__title = Slot(uri=DEFAULT_.title, name="codeSystem__title", curie=DEFAULT_.curie('title'),
                   model_uri=DEFAULT_.codeSystem__title, domain=None, range=Optional[str])

slots.codeSystem__homepage = Slot(uri=DEFAULT_.homepage, name="codeSystem__homepage", curie=DEFAULT_.curie('homepage'),
                   model_uri=DEFAULT_.codeSystem__homepage, domain=None, range=Optional[Union[str, URI]])

slots.coding__system = Slot(uri=DEFAULT_.system, name="coding__system", curie=DEFAULT_.curie('system'),
                   model_uri=DEFAULT_.coding__system, domain=None, range=str)

slots.coding__code = Slot(uri=DEFAULT_.code, name="coding__code", curie=DEFAULT_.curie('code'),
                   model_uri=DEFAULT_.coding__code, domain=None, range=str)

slots.coding__label = Slot(uri=DEFAULT_.label, name="coding__label", curie=DEFAULT_.curie('label'),
                   model_uri=DEFAULT_.coding__label, domain=None, range=Optional[str])

slots.valueSet__id = Slot(uri=DEFAULT_.id, name="valueSet__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.valueSet__id, domain=None, range=Union[str, Curie])

slots.valueSet__label = Slot(uri=DEFAULT_.label, name="valueSet__label", curie=DEFAULT_.curie('label'),
                   model_uri=DEFAULT_.valueSet__label, domain=None, range=str)

slots.valueSet__codes = Slot(uri=DEFAULT_.codes, name="valueSet__codes", curie=DEFAULT_.curie('codes'),
                   model_uri=DEFAULT_.valueSet__codes, domain=None, range=Optional[Union[Union[dict, Coding], list[Union[dict, Coding]]]])

slots.dataElement__ordinal = Slot(uri=DEFAULT_.ordinal, name="dataElement__ordinal", curie=DEFAULT_.curie('ordinal'),
                   model_uri=DEFAULT_.dataElement__ordinal, domain=None, range=str)

slots.dataElement__section = Slot(uri=DEFAULT_.section, name="dataElement__section", curie=DEFAULT_.curie('section'),
                   model_uri=DEFAULT_.dataElement__section, domain=None, range=Optional[str])

slots.dataElement__elementName = Slot(uri=DEFAULT_.elementName, name="dataElement__elementName", curie=DEFAULT_.curie('elementName'),
                   model_uri=DEFAULT_.dataElement__elementName, domain=None, range=str)

slots.dataElement__elementCode = Slot(uri=DEFAULT_.elementCode, name="dataElement__elementCode", curie=DEFAULT_.curie('elementCode'),
                   model_uri=DEFAULT_.dataElement__elementCode, domain=None, range=Union[dict, Coding])

slots.dataElement__elementCodeSystem = Slot(uri=DEFAULT_.elementCodeSystem, name="dataElement__elementCodeSystem", curie=DEFAULT_.curie('elementCodeSystem'),
                   model_uri=DEFAULT_.dataElement__elementCodeSystem, domain=None, range=str)

slots.dataElement__dataType = Slot(uri=DEFAULT_.dataType, name="dataElement__dataType", curie=DEFAULT_.curie('dataType'),
                   model_uri=DEFAULT_.dataElement__dataType, domain=None, range=Optional[str])

slots.dataElement__dataSpecification = Slot(uri=DEFAULT_.dataSpecification, name="dataElement__dataSpecification", curie=DEFAULT_.curie('dataSpecification'),
                   model_uri=DEFAULT_.dataElement__dataSpecification, domain=None, range=Optional[Union[str, list[str]]])

slots.dataElement__valueSet = Slot(uri=DEFAULT_.valueSet, name="dataElement__valueSet", curie=DEFAULT_.curie('valueSet'),
                   model_uri=DEFAULT_.dataElement__valueSet, domain=None, range=Optional[str])

slots.dataElement__fhirExpression_v4_0_1 = Slot(uri=DEFAULT_.fhirExpression_v4_0_1, name="dataElement__fhirExpression_v4_0_1", curie=DEFAULT_.curie('fhirExpression_v4_0_1'),
                   model_uri=DEFAULT_.dataElement__fhirExpression_v4_0_1, domain=None, range=Optional[str])

slots.dataElement__recommendedDataSpec_fhir = Slot(uri=DEFAULT_.recommendedDataSpec_fhir, name="dataElement__recommendedDataSpec_fhir", curie=DEFAULT_.curie('recommendedDataSpec_fhir'),
                   model_uri=DEFAULT_.dataElement__recommendedDataSpec_fhir, domain=None, range=Optional[str])

slots.dataElement__phenopacketSchemaElement_v2_0 = Slot(uri=DEFAULT_.phenopacketSchemaElement_v2_0, name="dataElement__phenopacketSchemaElement_v2_0", curie=DEFAULT_.curie('phenopacketSchemaElement_v2_0'),
                   model_uri=DEFAULT_.dataElement__phenopacketSchemaElement_v2_0, domain=None, range=Optional[str])

slots.dataElement__recommendedDataSpec_phenopackets = Slot(uri=DEFAULT_.recommendedDataSpec_phenopackets, name="dataElement__recommendedDataSpec_phenopackets", curie=DEFAULT_.curie('recommendedDataSpec_phenopackets'),
                   model_uri=DEFAULT_.dataElement__recommendedDataSpec_phenopackets, domain=None, range=Optional[str])

slots.dataElement__description = Slot(uri=DEFAULT_.description, name="dataElement__description", curie=DEFAULT_.curie('description'),
                   model_uri=DEFAULT_.dataElement__description, domain=None, range=Optional[str])

