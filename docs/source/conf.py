# Configuration file for the Sphinx documentation builder.
# See: https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path

# ── Path setup: make the project root importable ───────────────────────────────
# conf.py lives in: <repo_root>/docs/source/conf.py
# Project root is therefore two levels up from this file.
ROOT = Path(__file__).resolve().parents[2]   # -> <repo_root>
sys.path.insert(0, str(ROOT))

# ── Django setup so autodoc can import your project ────────────────────────────
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "minions_site.settings")  # <-- adjust if needed
try:
    import django  # type: ignore
    django.setup()
except Exception as e:
    # Avoid hard-failing during edits if Django isn't available yet
    print(f"[sphinx/conf.py] Django setup skipped/failed: {e}")

# ── Project information ────────────────────────────────────────────────────────
project = "Minions_Project"
author = "Minnie"
copyright = "2025, Minnie"
release = "2025"
language = "en"

# ── General configuration ─────────────────────────────────────────────────────
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",   # Google/NumPy-style docstrings
    "sphinx.ext.viewcode",   # link to highlighted source
]
autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# ── HTML output ───────────────────────────────────────────────────────────────
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 3,
}
