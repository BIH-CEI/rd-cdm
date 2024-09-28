from dataclasses import dataclass, field

from .base_types import CodeSystem

# Function to create a list of CodeSystem instances without versions
def create_code_systems(versions: dict[str, str]):
    """Create a list of CodeSystem instances and filter by defined versions."""
    
    all_code_systems = [
        CodeSystem(
            name="NCBI organismal classification", 
            namespace_prefix="NCBITaxon", 
            url="https://www.ncbi.nlm.nih.gov/taxonomy"
        ),
        CodeSystem(
            name="GENO: The Genotype Ontology", 
            namespace_prefix="GENO", 
            url="http://www.genoontology.org/"
        ),
        CodeSystem(
            name="Sequence types and features ontology", 
            namespace_prefix="SO", 
            url="http://www.sequenceontology.org/"
        ),
        CodeSystem(
            name="International Classification of Diseases, Ninth Revision", 
            namespace_prefix="ICD9", 
            url="https://www.cdc.gov/nchs/icd/icd9.htm", 
            synonyms=["ICD-9", "ICD_9"]
        ),
        CodeSystem(
            name="International Classification of Diseases, Tenth Revision, "
                 "German Modification", 
            namespace_prefix="ICD10GM", 
            url="https://www.bfarm.de/EN/Code-systems/Classifications/ICD/"
                 "ICD-10-GM/_node.html", 
            synonyms=["ICD10-GM", "ICD-10-GM", "ICD10_GM", "ICD_10_GM"]
        ),
        CodeSystem(
            name="International Classification of Diseases, Tenth Revision, "
                 "Clinical Modification", 
            namespace_prefix="ICD10CM", 
            url="https://www.cdc.gov/nchs/icd/icd10cm.htm", 
            synonyms=["ICD10-CM", "ICD10_CM", "ICD-10-CM", "ICD_10_CM"]
        ),
        CodeSystem(
            name="SNOMED", 
            namespace_prefix="SNOMED", 
            url="https://www.snomed.org/snomed-ct", 
            synonyms=["SCT", "SNOMED CT"]
        ),
        CodeSystem(
            name="International Classification of Diseases, Eleventh Revision", 
            namespace_prefix="ICD11", 
            url="https://icd.who.int/en", 
            synonyms=["ICD-11"]
        ),
        CodeSystem(
            name="Health Level 7 Fast Healthcare Interoperability Resources", 
            namespace_prefix="HL7FHIR", 
            url="https://www.hl7.org/fhir/"
        ),
        CodeSystem(
            name="Global Alliance for Genomics and Health Phenopacket Schema v2.0", 
            namespace_prefix="GA4GH", 
            url="https://www.ga4gh.org/product/phenopackets/"
        ),
        CodeSystem(
            name="ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes", 
            namespace_prefix="ISO3166", 
            url="https://www.iso.org/iso-3166-country-codes.html"
        ),
        CodeSystem(
            name="International Classification of Functioning, Disability and "
                 "Health (ICF)", 
            namespace_prefix="ICF", 
            url="https://www.who.int/classifications/icf/en/"
        ),
        CodeSystem(
            name="Monarch Disease Ontology", 
            namespace_prefix="MONDO", 
            url="http://purl.obolibrary.org/obo/mondo.owl"
        ),
        CodeSystem(
            name="Orphanet Rare Disease Ontology", 
            namespace_prefix="ORDO", 
            url="http://www.orpha.net/", 
            synonyms=["ORPHA"]
        ),
        CodeSystem(
            name="Online Mendelian Inheritance", 
            namespace_prefix="OMIM", 
            url="https://omim.org/"
        ),
        CodeSystem(
            name="Logical Observation Identifiers Names and Codes", 
            namespace_prefix="LOINC", 
            url="https://loinc.org/"
        ),
        CodeSystem(
            name="Human Genome Variation Society", 
            namespace_prefix="HGVS", 
            url="http://varnomen.hgvs.org/"
        ),
        CodeSystem(
            name="HUGO Gene Nomenclature Committee", 
            namespace_prefix="HGNC", 
            url="https://www.genenames.org/"
        ),
        CodeSystem(
            name="Human Phenotype Ontology", 
            namespace_prefix="HP", 
            url="http://www.human-phenotype-ontology.org", 
            iri_prefix="http://purl.obolibrary.org/obo/HP_", 
            synonyms=["HPO"]
        ),
        CodeSystem(
            name="Units of Measurement Ontology", 
            namespace_prefix="UO", 
            url="http://www.ontobee.org/ontology/UO"
        ),
        CodeSystem(
            name="NCI Thesaurus OBO Edition", 
            namespace_prefix="NCIT", 
            url="https://ncit.nci.nih.gov/"
        )
    ]
    
    # Filter code systems to include only those with a defined version
    filtered_code_systems = [
        cs for cs in all_code_systems if cs.namespace_prefix in versions
    ]

    return filtered_code_systems