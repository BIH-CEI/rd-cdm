import types
import pytest

from rd_cdm.utils import validation_utils as vu


def test_clean_code_basic():
    assert vu.clean_code("  123-45.6  ") == "123-45.6"
    assert vu.clean_code("HP:0000118") == "HP0000118"  # colon removed
    assert vu.clean_code("abc_DEF") == "abcDEF"        # underscore removed
    assert vu.clean_code("00A-01") == "00A-01"         # leading zeros kept


def test_bp_headers_requires_env(monkeypatch, capsys):
    monkeypatch.delenv("BIOPORTAL_API_KEY", raising=False)
    with pytest.raises(SystemExit) as e:
        vu.bp_headers()
    assert e.value.code == 2
    out = capsys.readouterr().err
    assert "BIOPORTAL_API_KEY not set" in out

    monkeypatch.setenv("BIOPORTAL_API_KEY", "TESTKEY")
    hdrs = vu.bp_headers()
    assert hdrs["Authorization"] == "apikey token=TESTKEY"


class _Resp:
    def __init__(self, status, payload):
        self.status_code = status
        self._payload = payload
    def json(self):
        return self._payload
    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise RuntimeError(f"HTTP {self.status_code}")


def test_get_remote_version(monkeypatch):
    # two calls: /ontologies/{sys} -> meta with latest_submission
    # then GET latest_submission -> version payload
    calls = {"count": 0}
    def fake_get(url, headers=None):
        calls["count"] += 1
        if url.endswith("/ontologies/HP"):
            return _Resp(200, {"links": {"latest_submission": "http://x/submissions/last"}})
        elif url.endswith("/submissions/last"):
            return _Resp(200, {"version": "2025-04-01"})
        return _Resp(404, {})
    monkeypatch.setenv("BIOPORTAL_API_KEY", "X")
    monkeypatch.setattr(vu, "requests", types.SimpleNamespace(get=fake_get))
    assert vu.get_remote_version("HP") == "2025-04-01"
    assert calls["count"] == 2


def test_get_remote_label_curie_then_iri(monkeypatch):
    # First try CURIE -> 404, then try IRI path -> 200 with prefLabel.
    def fake_get(url, headers=None):
        if "/classes/HP%3A0000118" in url:   # CURIE try
            return _Resp(404, {})
        if "/ontologies/HP/classes/" in url: # IRI try
            return _Resp(200, {"prefLabel": "Phenotypic abnormality"})
        return _Resp(500, {})
    monkeypatch.setenv("BIOPORTAL_API_KEY", "X")
    monkeypatch.setattr(vu, "requests", types.SimpleNamespace(get=fake_get))
    label = vu.get_remote_label("HP", "HP:0000118", "http://purl.obolibrary.org/obo/HP_")
    assert label == "Phenotypic abnormality"

    # composite code → None (skipped)
    assert vu.get_remote_label("HP", "HP:0000118=foo", "http://x") is None
