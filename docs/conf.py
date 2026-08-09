import doctest
import os
import sys

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.insert(0, src_path)


project = 'Ontology-based rare disease common data model (RD-CDM)'
copyright = 'Berlin Institute of Health, Charité Universitätsmedizin Berlin'
author = 'Adam S.L. Graefe'

try:
    from rd_cdm.utils.versioning import get_model_version

    release = get_model_version() or 'unknown'
except Exception:
    release = 'unknown'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'myst_parser',
    'sphinxcontrib.mermaid',
]

# gen-doc emits Markdown; myst renders it alongside the hand-written reST.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
myst_heading_anchors = 3

# gen-doc puts a mermaid class diagram on each class page as a fenced block.
# Without this it is treated as a code block with an unknown lexer, which warns
# and renders the diagram source as text.
myst_fence_as_directive = ['mermaid']

# gen-doc writes one page per class, slot and enum, linked from
# datamodel/index.md rather than from a toctree. Without this every generated
# page raises "document isn't included in any toctree" and buries real warnings.
suppress_warnings = ['toc.not_included']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

# -- Autodoc setup ------------------------------------------------------------

autodoc_member_order = 'bysource'

# -- Doctest setup ------------------------------------------------------------

doctest_path = [src_path]
doctest_test_doctest_blocks = ""

doctest_default_flags = (doctest.REPORT_ONLY_FIRST_FAILURE
                         | doctest.ELLIPSIS
                         | doctest.IGNORE_EXCEPTION_DETAIL
                         | doctest.DONT_ACCEPT_TRUE_FOR_1)


# -- Intersphinx setup --------------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/version/2.0.0/", None),
    "requests": ("https://docs.python-requests.org/en/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy-1.11.0/", None),
    "statsmodels": ("https://www.statsmodels.org/stable/", None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # experiment with this
html_static_path = ['_static']
html_css_files = [
    'custom.css',  # Include your custom CSS
]
html_theme_options = {
    'collapse_navigation': False,  # Prevents collapsing sections
    'navigation_depth': -1,        # Shows all levels of navigation
    'titles_only': False           # Includes all subsections, not just titles
}