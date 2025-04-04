# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup ---------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(".."))


# -- Project information ------------------------------------------------------

project = "pyaqsapi"
copyright = "2025, US Environmental Protection Agency"
author = "Clinton Mccrowey (US Environmental Protection Agency)"


# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # "sphinx.ext.autodoc",
    "sphinxcontrib.apidoc",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    # the dependencies required for sphinxcontrib.spelling
    # do not seem to be maintained anymore
    # "sphinxcontrib.spelling",
    "numpydoc",
    "sphinx.ext.napoleon",
    "sphinxcontrib.bibtex",
    "sphinx.ext.autosectionlabel",
]

# sphinxcontrib.bibtex bibtext file location
bibtex_bibfiles = ["manual/pyaqsapi.bib"]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "setup.py"]

# get rid of those duplicate label warnings when embedding a child rst file
# into another rst file.
suppress_warnings = ["autosectionlabel"]

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Options for sphinxcontrib.bibtex -----------------------------------------
bibtex_reference_style = "label"
bibtex_default_style = "plain"
bibtex_tooltips = True

# -- Options for Napolean output ---------------------------------------------
napolean_include_private_with_doc = False
napolean_include_special_with_doc = False
napoleon_include_init_with_doc = False
napolean_use_param = True
napolean_use_rtype = True
napolean_reprocess_types = True
napoleon_google_docstring = True
# napoleon_numpy_docstring = True

# the dependencies required for sphinxcontrib.spelling
# do not seem to be maintained anymore
# -- Options for sphinxcontrib-spelling ---------------------------------------
# spelling_lang = "en_US"
# tokenizer_lang = "en_US"
# spelling_word_list_filename = "ignored_wordlist.txt"
# spelling_show_suggestions = True
# spelling_show_whole_line = True
# spelling_warning = True
# spelling_verbose = True
# spelling_ignore_pypi_package_names = True
# spelling_ignore_python_builtins = True
# spelling_ignore_contributor_names = True

# -- Options for numpydoc -----------------------------------------------------
numpydoc_show_class_members = False

# -- Options for sphinx-contrib\apidoc, sphinxcontrib\autodoc------------------
apidoc_separate_modules = False
apidoc_module_dir = "../pyaqsapi"
apidoc_excluded_paths = ["tests"]
apidoc_module_first = True
apidoc_toc_file = "modules"
apidoc_output_dir = "."
autodoc_typehints = "both"
