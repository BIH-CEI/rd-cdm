import os
import sys
import re
from urllib.parse import quote
import requests
BP_BASE = "https://data.bioontology.org"

def clean_code(raw) -> str:
    """
    Normalize a raw ontology code into the minimal token that BioPortal will accept.

    Behavior:
    - Casts any input to a string.
    - Removes all characters except letters, digits, dots, and hyphens.
      (SNOMED CT and LOINC IDs frequently include only these symbols.)
    - Does NOT strip meaningful leading zeros.
    - Does NOT attempt to interpret composite SNOMED expressions; those are
      handled by the caller (and usually skipped).

    Parameters
    ----------
    raw : Any
        The raw code value as found in the YAML (may be str, int, etc).

    Returns
    -------
    str
        A cleaned string suitable for lookup against BioPortal.
    """
    s = str(raw)
    return re.sub(r'[^A-Za-z0-9\.-]', '', s)

def bp_headers():
    """
    Build the HTTP headers required for calling the BioPortal REST API.

    Reads the API key from the environment variable BIOPORTAL_API_KEY and
    formats the Authorization header as:
        Authorization: apikey token=<BIOPORTAL_API_KEY>

    Exits the process with code 2 if the variable is missing, because without
    it all calls to https://data.bioontology.org will fail with 401.

    Returns
    -------
    dict[str, str]
        Headers dict suitable for requests.get(..., headers=bp_headers()).
    """
    key = os.getenv("BIOPORTAL_API_KEY")
    if not key:
        print("ERROR: BIOPORTAL_API_KEY not set", file=sys.stderr)
        sys.exit(2)
    return {"Authorization": f"apikey token={key}"}

def get_remote_version(sys_id: str) -> str:
    """
    Fetch the latest published version string for an ontology from BioPortal.

    Workflow:
    1) GET /ontologies/{sys_id} to discover the 'latest_submission' link.
    2) GET that latest_submission resource.
    3) Return the first populated field among: 'version', 'versionNumber',
       or 'submissionDate'. If none are present, '<unknown>' is returned.

    Notes
    -----
    - Uses the same ontology id that appears in your CodeSystem.id
      (e.g., 'HP', 'NCIT', 'SNOMEDCT', 'LOINC').
    - Network/HTTP errors are allowed to bubble up to the caller; callers
      can catch requests.HTTPError or general Exception and decide whether
      to treat it as a warning or an error.

    Parameters
    ----------
    sys_id : str
        BioPortal ontology acronym (e.g., 'HP', 'NCIT', 'SNOMEDCT', 'LOINC').

    Returns
    -------
    str
        Version string reported by BioPortal for the latest submission,
        or '<unknown>' if none could be determined.

    Raises
    ------
    requests.HTTPError
        If BioPortal returns a non-2xx status other than 404 on the calls.
    RuntimeError
        If the ontology record has no 'latest_submission' link.
    """
    url_meta = f"{BP_BASE}/ontologies/{sys_id}"
    r_meta = requests.get(url_meta, headers=bp_headers())
    r_meta.raise_for_status()
    meta = r_meta.json()
    latest_url = meta.get("links", {}).get("latest_submission")
    if not latest_url:
        raise RuntimeError(f"No latest_submission link for {sys_id}")
    r_sub = requests.get(latest_url, headers=bp_headers())
    r_sub.raise_for_status()
    sub = r_sub.json()
    return sub.get("version") or sub.get("versionNumber") or sub.get("submissionDate") or "<unknown>"

def get_remote_label(sys_id: str, code: str, namespace_iri: str) -> str | None:
    """
    Resolve a code to its preferred label ('prefLabel') via the BioPortal API.

    Resolution strategy (mirrors the working RareLink behavior):
    1) Try CURIE lookup directly: /ontologies/{sys_id}/classes/{quote(sys_id:code)}
       - Works for ontologies that accept CURIE identifiers.
       - 200 → return 'prefLabel'; 404 → fall through; other → raise_for_status().
    2) Try an ontology-specific full IRI using a hard-coded mapping:
       - ORPHA → ORDO IRI (http://www.orpha.net/ORDO/Orphanet_{code})
       - HGNC  → HGNC-NR IRI (http://identifiers.org/hgnc/{code})
       - NCIT  → EVS Thesaurus IRI (http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#{code})
       - NCBITAXON, HP, MONDO, OMIM, ECO, UO, VO, GENO → OBO-style IRIs
       - ICD10CM, SNOMEDCT, LOINC → use the identifier *as-is* (BioPortal accepts IDs for these)
       - If no mapping exists, build a fallback IRI as {namespace_iri.rstrip('/')}/{code}
       - 200 → return 'prefLabel'; 404 → return None; other → raise_for_status().

    Special cases
    -------------
    - If the code contains '=', we treat it as a composite (e.g., SNOMED CT ECL
      or post-coordinated expression) and return None so the caller can skip it.
    - The function does not compare labels or versions; it only resolves to a
      single string prefLabel when possible.

    Parameters
    ----------
    sys_id : str
        Ontology acronym (e.g., 'SNOMEDCT', 'LOINC', 'HP', 'NCIT').
    code : str
        Identifier part (already cleaned by the caller). May contain letters,
        digits, dots, and hyphens. If '=' is present, the call is skipped.
    namespace_iri : str
        Default base IRI for the ontology, used only as a fallback when no
        ontology-specific mapping is defined.

    Returns
    -------
    str | None
        The 'prefLabel' if found; otherwise None.

    Raises
    ------
    requests.HTTPError
        If BioPortal returns a non-2xx status other than 404 for either request.
    """

    # 0) skip composite codes
    if not code or "=" in code:
        return None

    headers = bp_headers()

    # Build the ontology_map exactly as in RareLink
    ontology_map = {
        "ORPHA":     {"api": "ORDO",     "iri": f"http://www.orpha.net/ORDO/Orphanet_{code}"},
        "HGNC":      {"api": "HGNC-NR",  "iri": f"http://identifiers.org/hgnc/{code}"},
        "NCIT":      {"api": "NCIT",     "iri": f"http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#{code}"},
        "NCBITAXON": {"api": "NCBITAXON","iri": f"http://purl.bioontology.org/ontology/NCBITAXON/{code}"},
        "HP":        {"api": "HP",       "iri": f"http://purl.obolibrary.org/obo/HP_{code.replace(':','_')}"},
        "ICD10CM":   {"api": "ICD10CM",  "iri": code},  # use identifier as‐is
        "SNOMEDCT":  {"api": "SNOMEDCT", "iri": code},  # use identifier as‐is
        "LOINC":     {"api": "LOINC",    "iri": code},  # use identifier as‐is
        "MONDO":     {"api": "MONDO",    "iri": f"http://purl.obolibrary.org/obo/MONDO_{code.replace(':','_')}"},
        "OMIM":      {"api": "OMIM",     "iri": f"http://purl.bioontology.org/ontology/OMIM/{code}"},
        "ECO":       {"api": "ECO",      "iri": f"http://purl.obolibrary.org/obo/ECO_{code}"},
        "UO":        {"api": "UO",       "iri": f"http://purl.obolibrary.org/obo/UO_{code}"},
        "VO":        {"api": "VO",       "iri": f"http://purl.obolibrary.org/obo/VO_{code}"},
        "GENO":      {"api": "GENO",     "iri": f"http://purl.obolibrary.org/obo/GENO_{code}"}
    }

    # 1) Try lookup by raw CURIE first
    curie = f"{sys_id}:{code}"
    url_curie = f"{BP_BASE}/ontologies/{sys_id}/classes/{quote(curie, safe='')}"
    r = requests.get(url_curie, headers=headers)
    if r.status_code == 200:
        return r.json().get("prefLabel")
    if r.status_code not in (404,):
        r.raise_for_status()

    # 2) Fall back to the mapped IRI for this ontology (or default to namespace_iri/code)
    m = ontology_map.get(sys_id)
    if m:
        api_onto = m["api"]
        iri      = m["iri"]
    else:
        api_onto = sys_id
        iri      = f"{namespace_iri.rstrip('/')}/{code}"
    url_iri = f"{BP_BASE}/ontologies/{api_onto}/classes/{quote(iri, safe='')}"
    r2 = requests.get(url_iri, headers=headers)
    if r2.status_code == 200:
        return r2.json().get("prefLabel")
    if r2.status_code not in (404,):
        r2.raise_for_status()

    return None