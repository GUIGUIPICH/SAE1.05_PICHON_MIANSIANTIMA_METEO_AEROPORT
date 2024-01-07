# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Météo d'un aéroport"
copyright = '2024, Guillaume PICHON - Promisse MIANSIANTIMA'
author = 'Guillaume PICHON - Promisse MIANSIANTIMA'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
'sphinx.ext.todo',
'sphinx.ext.mathjax',
'sphinx.ext.ifconfig',
'sphinx.ext.autodoc',
'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import sys
sys.path.insert(0, '/home/guillaume/Documents/SAE1.05_PICHON_MIANSIANTIMA_METEO_AEROPORT/meteo_aeroport')
