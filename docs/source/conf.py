import pytower
from datetime import datetime

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'PyTower'
copyright = f'{datetime.now().year}, Rainbow Physics'
author = 'Rainbow Physics'

release = f'{pytower.__version__}'[:-2]
version = f'{pytower.__version__}'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

autosummary_generate = True
autosummary_generate_overwrite = False
autosummary_imported_members = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'
