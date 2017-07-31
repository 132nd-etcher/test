#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# EMFT documentation build configuration file, created by
# sphinx-quickstart on Mon Jul 17 12:44:24 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from src.__version_frozen__ import __version__, __pep440__  # noqa: E402

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx_autodoc_typehints',
              'sphinx_git',
              'sphinx.ext.intersphinx',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'sphinx.ext.todo',
              'sphinxjp.themes.basicstrap',
              'sphinx_click.ext',
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'EMFT'
copyright = '2017, 132nd-etcher'
author = '132nd-etcher'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
version = release = f'{__version__}\n({__pep440__})'
# version = __pep440__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# # -- Guzzle theme conf ----------------------------------------------------------------------
# import guzzle_sphinx_theme
# html_theme_path = guzzle_sphinx_theme.html_theme_path()
# html_theme = 'guzzle_sphinx_theme'
# extensions.append("guzzle_sphinx_theme")
#
# html_theme_options = {
#     # Set the name of the project to appear in the sidebar
#     "project_nav_name": "EMFT",
# }

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.

# -- Alabaster theme conf -------------------------------------------------
# html_theme = 'alabaster'
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'relations.html',  # needs 'show_related': True theme option to display
#         'searchbox.html',
#         'donate.html',
#     ]
# }


# -- RTD theme conf -------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'collapse_navigation': True,
    'display_version': True,
    'navigation_depth': 3,
}

# -- Options for HTML output --------------------------

# # -- HTML theme options for `basicstrap` style -------
# # https://pythonhosted.org/sphinxjp.themes.basicstrap/index.html
# html_theme = 'basicstrap'
# html_theme_options = {
#
#     # Set the lang attribute of the html tag. Defaults to 'en'
#     'lang': 'en',
#     # Disable showing the sidebar. Defaults to 'false'
#     'nosidebar': False,
#     # Show header searchbox. Defaults to false. works only "nosidber=True",
#     'header_searchbox': True,
#
#     # Put the sidebar on the right side. Defaults to false.
#     'rightsidebar': False,
#     # Set the width of the sidebar. Defaults to 3
#     'sidebar_span': 3,
#
#     # Fix navbar to top of screen. Defaults to true
#     'nav_fixed_top': True,
#     # Fix the width of the sidebar. Defaults to false
#     'nav_fixed': False,
#     # Set the width of the sidebar. Defaults to '900px'
#     'nav_width': '900px',
#     # Fix the width of the content area. Defaults to false
#
#     'content_fixed': False,
#     # Set the width of the content area. Defaults to '900px'
#     'content_width': '900px',
#     # Fix the width of the row. Defaults to false
#     'row_fixed': False,
#
#     # Disable the responsive design. Defaults to false
#     'noresponsive': False,
#     # Disable the responsive footer relbar. Defaults to false
#     'noresponsiverelbar': False,
#     # Disable flat design. Defaults to false.
#     # Works only "bootstrap_version = 3"
#     'noflatdesign': False,
#
#     # Enable Google Web Font. Defaults to false
#     'googlewebfont': True,
#     # Set the URL of Google Web Font's CSS.
#     # Defaults to 'http://fonts.googleapis.com/css?family=Text+Me+One'
#     'googlewebfont_url': 'https://fonts.googleapis.com/css?family=Inconsolata',  # NOQA
#     # Set the Style of Google Web Font's CSS.
#     # Defaults to "font-family: 'Text Me One', sans-serif;"
#     'googlewebfont_style': u"font-family: 'Inconsolata', monospace;",
#
#     # Set 'navbar-inverse' attribute to header navbar. Defaults to false.
#     'header_inverse': True,
#     # Set 'navbar-inverse' attribute to relbar navbar. Defaults to false.
#     'relbar_inverse': True,
#
#     # Enable inner theme by Bootswatch. Defaults to false
#     'inner_theme': True,
#     # Set the name of innner theme. Defaults to 'bootswatch-simplex'
#     'inner_theme_name': 'bootswatch-journal',
#
#     # Select Twitter bootstrap version 2 or 3. Defaults to '3'
#     'bootstrap_version': '3',
#
#     # Show "theme preview" button in header navbar. Defaults to false.
#     'theme_preview': False,
#
#     # Set the Size of Heading text. Defaults to None
#     # 'h1_size': '3.0em',
#     # 'h2_size': '2.6em',
#     # 'h3_size': '2.2em',
#     # 'h4_size': '1.8em',
#     # 'h5_size': '1.4em',
#     # 'h6_size': '1.1em',
# }


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'EMFTdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'EMFT.tex', 'EMFT Documentation',
     '132nd-etcher', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'emft', 'EMFT Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'EMFT', 'EMFT Documentation',
     author, 'EMFT', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
