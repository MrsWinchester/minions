# Configuration file for the Sphinx documentation builder.

# --- Django setup so autodoc can import your project ---
import os
import sys
import django

# If conf.py is in docs_src/, go up one level to the project root:
sys.path.insert(0, os.path.abspath('..'))

# Point to your Django settings module:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minions_site.settings')

# Initialise Django (required before importing project code)
django.setup()

# --- Project information ---
project = 'The Minions'
author = 'Your Name'
copyright = '2025, Your Name'
version = '1.0'
release = '1.0'

# --- General configuration ---
extensions = [
    'sphinx.ext.autodoc',   # pull docstrings from your code
    'sphinx.ext.napoleon',  # support Google/NumPy-style docstrings
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Optional: nicer type hints display
autodoc_typehints = 'description'
autodoc_member_order = 'bysource'

# --- HTML output options ---
html_theme = 'alabaster'
html_static_path = ['_static']
