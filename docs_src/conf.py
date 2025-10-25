# --- Django setup so autodoc can import your project ---
import os, sys, django
from pathlib import Path

# If conf.py is in docs_src/, this points to your repo root
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))                 # add project root
sys.path.insert(0, str(ROOT / "minions_site"))# also add the project package

# Match the value used in your manage.py:
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "minions_site.settings")
django.setup()

# --- Project info ---
project = "The Minions"
author = "Your Name"
copyright = "2025, Your Name"
version = "1.0"
release = "1.0"

# --- Sphinx extensions ---
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# (optional)
autodoc_typehints = "description"
autodoc_member_order = "bysource"

html_theme = "alabaster"
html_static_path = ["_static"]
