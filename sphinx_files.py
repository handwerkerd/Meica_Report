#!/usr/bin/env python
"""
Gutierrez, B.  Generates the analysis.rst file
"""

def conf(__version__):
	sl = []
	sl.append('# -*- coding: utf-8 -*-')
	sl.append('#')
	sl.append('# Test documentation build configuration file, created by')
	sl.append('# sphinx-quickstart on Fri Aug 22 09:13:04 2014.')
	sl.append('#')
	sl.append('# This file is execfile()d with the current directory set to its')
	sl.append('# containing dir.')
	sl.append('#')
	sl.append('# Note that not all possible configuration values are present in this')
	sl.append('# autogenerated file.')
	sl.append('#')
	sl.append('# All configuration values have a default; values that are commented out')
	sl.append('# serve to show the default.\n')

	sl.append('import sys')
	sl.append('import os\n')

	sl.append('# If extensions (or modules to document with autodoc) are in another directory,')
	sl.append('# add these directories to sys.path here. If the directory is relative to the')
	sl.append('# documentation root, use os.path.abspath to make it absolute, like shown here.')
	sl.append('#sys.path.insert(0, os.path.abspath(\'.\'))\n')

	sl.append('# -- General configuration ------------------------------------------------\n')

	sl.append('# If your documentation needs a minimal Sphinx version, state it here.')
	sl.append('#needs_sphinx = \'1.0\'\n')

	sl.append('# Add any Sphinx extension module names here, as strings. They can be')
	sl.append('# extensions coming with Sphinx (named \'sphinx.ext.*\') or your custom')
	sl.append('# ones.')
	sl.append('extensions = []\n')

	sl.append('# Add any paths that contain templates here, relative to this directory.')
	sl.append('templates_path = [\'_templates\']\n')

	sl.append('# The suffix of source filenames.')
	sl.append('source_suffix = \'.rst\'\n')

	sl.append('# The encoding of source files.')
	sl.append('#source_encoding = \'utf-8-sig\'\n')

	sl.append('# The master toctree document.')
	sl.append('master_doc = \'index\'\n')

	sl.append('# General information about the project.')
	sl.append('project = u\'Meica Report\'')
	sl.append('copyright = u\'2014, Prantik Kundu\'\n')

	sl.append('# The version info for the project you\'re documenting, acts as replacement for')
	sl.append('# |version| and |release|, also used in various other places throughout the')
	sl.append('# built documents.')
	sl.append('#')
	sl.append('# The short X.Y version.')
	sl.append('version = \'%s\'' % (__version__))
	sl.append('# The full version, including alpha/beta/rc tags.')
	sl.append('release = \'%s\'\n' % (__version__))

	sl.append('# The language for content autogenerated by Sphinx. Refer to documentation')
	sl.append('# for a list of supported languages.')
	sl.append('#language = None\n')

	sl.append('# There are two options for replacing |today|: either, you set today to some')
	sl.append('# non-false value, then it is used:')
	sl.append('#today = ''')
	sl.append('# Else, today_fmt is used as the format for a strftime call.')
	sl.append('#today_fmt = \'%sB %sd, %sY\'\n' % ('%','%','%'))

	sl.append('# List of patterns, relative to source directory, that match files and')
	sl.append('# directories to ignore when looking for source files.')
	sl.append('exclude_patterns = [\'_build\']\n')

	sl.append('# The reST default role (used for this markup: `text`) to use for all')
	sl.append('# documents.')
	sl.append('#default_role = None\n')

	sl.append('# If true, \'()\' will be appended to :func: etc. cross-reference text.')
	sl.append('#add_function_parentheses = True\n')

	sl.append('# If true, the current module name will be prepended to all description')
	sl.append('# unit titles (such as .. function::).')
	sl.append('#add_module_names = True\n')

	sl.append('# If true, sectionauthor and moduleauthor directives will be shown in the')
	sl.append('# output. They are ignored by default.')
	sl.append('#show_authors = False\n')

	sl.append('# The name of the Pygments (syntax highlighting) style to use.')
	sl.append('pygments_style = \'sphinx\'\n')

	sl.append('# A list of ignored prefixes for module index sorting.')
	sl.append('#modindex_common_prefix = []\n')

	sl.append('# If true, keep warnings as "system message" paragraphs in the built documents.')
	sl.append('#keep_warnings = False\n\n')


	sl.append('# -- Options for HTML output ----------------------------------------------\n')

	sl.append('# The theme to use for HTML and HTML Help pages.  See the documentation for')
	sl.append('# a list of builtin themes.')
	sl.append('html_theme = \'default\'\n')

	sl.append('# Theme options are theme-specific and customize the look and feel of a theme')
	sl.append('# further.  For a list of options available for each theme, see the')
	sl.append('# documentation.')
	sl.append('#html_theme_options = {}\n')

	sl.append('# Add any paths that contain custom themes here, relative to this directory.')
	sl.append('#html_theme_path = []\n')

	sl.append('# The name for this set of Sphinx documents.  If None, it defaults to')
	sl.append('# "<project> v<release> documentation".')
	sl.append('#html_title = None\n')

	sl.append('# A shorter title for the navigation bar.  Default is the same as html_title.')
	sl.append('#html_short_title = None\n')

	sl.append('# The name of an image file (relative to this directory) to place at the top')
	sl.append('# of the sidebar.')
	sl.append('#html_logo = None\n')

	sl.append('# The name of an image file (within the static path) to use as favicon of the')
	sl.append('# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32')
	sl.append('# pixels large.')
	sl.append('#html_favicon = None\n')

	sl.append('# Add any paths that contain custom static files (such as style sheets) here,')
	sl.append('# relative to this directory. They are copied after the builtin static files,')
	sl.append('# so a file named "default.css" will overwrite the builtin "default.css".')
	sl.append('html_static_path = [\'_static\']\n')

	sl.append('# Add any extra paths that contain custom files (such as robots.txt or')
	sl.append('# .htaccess) here, relative to this directory. These files are copied')
	sl.append('# directly to the root of the documentation.')
	sl.append('#html_extra_path = []\n')

	sl.append('# If not \'\', a \'Last updated on:\' timestamp is inserted at every page bottom,')
	sl.append('# using the given strftime format.')
	sl.append('#html_last_updated_fmt = \'%sb %sd, %sY\'\n' % ('%','%','%'))

	sl.append('# If true, SmartyPants will be used to convert quotes and dashes to')
	sl.append('# typographically correct entities.')
	sl.append('#html_use_smartypants = True\n')

	sl.append('# Custom sidebar templates, maps document names to template names.')
	sl.append('#html_sidebars = {}\n')

	sl.append('# Additional templates that should be rendered to pages, maps page names to')
	sl.append('# template names.')
	sl.append('#html_additional_pages = {}\n')

	sl.append('# If false, no module index is generated.')
	sl.append('#html_domain_indices = True\n')

	sl.append('# If false, no index is generated.')
	sl.append('#html_use_index = True\n')

	sl.append('# If true, the index is split into individual pages for each letter.')
	sl.append('#html_split_index = False\n')

	sl.append('# If true, links to the reST sources are added to the pages.')
	sl.append('#html_show_sourcelink = True\n')

	sl.append('# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.')
	sl.append('#html_show_sphinx = True\n')

	sl.append('# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.')
	sl.append('#html_show_copyright = True\n')

	sl.append('# If true, an OpenSearch description file will be output, and all pages will')
	sl.append('# contain a <link> tag referring to it.  The value of this option must be the')
	sl.append('# base URL from which the finished HTML is served.')
	sl.append('#html_use_opensearch = \'\'\n')

	sl.append('# This is the file name suffix for HTML files (e.g. ".xhtml").')
	sl.append('#html_file_suffix = None\n')

	sl.append('# Output file base name for HTML help builder.')
	sl.append('htmlhelp_basename = \'MeicaReportdoc\'\n\n\n')


	sl.append('# -- Options for LaTeX output ---------------------------------------------\n')

	sl.append('latex_elements = {')
	sl.append('# The paper size (\'letterpaper\' or \'a4paper\').')
	sl.append('#\'papersize\': \'letterpaper\',\n')

	sl.append('# The font size (\'10pt\', \'11pt\' or \'12pt\').')
	sl.append('#\'pointsize\': \'10pt\',\n')

	sl.append('# Additional stuff for the LaTeX preamble.')
	sl.append('#\'preamble\': \'\',')
	sl.append('}\n')

	sl.append('# Grouping the document tree into LaTeX files. List of tuples')
	sl.append('# (source start file, target name, title,')
	sl.append('#  author, documentclass [howto, manual, or own class]).')
	sl.append('latex_documents = [')
	sl.append('  (\'index\', \'MeicaReport.tex\', u\'Meica Report Documentation\',')
	sl.append('   u\'Prantik Kundu\', \'manual\'),')
	sl.append(']\n')

	sl.append('# The name of an image file (relative to this directory) to place at the top of')
	sl.append('# the title page.')
	sl.append('#latex_logo = None\n')

	sl.append('# For "manual" documents, if this is true, then toplevel headings are parts,')
	sl.append('# not chapters.')
	sl.append('#latex_use_parts = False\n')

	sl.append('# If true, show page references after internal links.')
	sl.append('#latex_show_pagerefs = False\n')

	sl.append('# If true, show URL addresses after external links.')
	sl.append('#latex_show_urls = False\n')

	sl.append('# Documents to append as an appendix to all manuals.')
	sl.append('#latex_appendices = []\n')

	sl.append('# If false, no module index is generated.')
	sl.append('#latex_domain_indices = True\n\n')


	sl.append('# -- Options for manual page output ---------------------------------------\n')

	sl.append('# One entry per manual page. List of tuples')
	sl.append('# (source start file, name, description, authors, manual section).')
	sl.append('man_pages = [')
	sl.append('    (\'index\', \'meicareport\', u\'Meica Report Documentation\',')
	sl.append('     [u\'Prantik Kundu\'], 1)')
	sl.append(']\n')

	sl.append('# If true, show URL addresses after external links.')
	sl.append('#man_show_urls = False\n\n')


	sl.append('# -- Options for Texinfo output -------------------------------------------\n')

	sl.append('# Grouping the document tree into Texinfo files. List of tuples')
	sl.append('# (source start file, target name, title, author,')
	sl.append('#  dir menu entry, description, category)')
	sl.append('texinfo_documents = [')
	sl.append('  (\'index\', \'MeicaReport\', u\'Meica Report Documentation\',')
	sl.append('   u\'Prantik Kundu\', \'MeicaReport\', \'One line description of project.\',')
	sl.append('   \'Miscellaneous\'),')
	sl.append(']\n')

	sl.append('# Documents to append as an appendix to all manuals.')
	sl.append('#texinfo_appendices = []\n')

	sl.append('# If false, no module index is generated.')
	sl.append('#texinfo_domain_indices = True\n')

	sl.append('# How to display URL addresses: \'footnote\', \'no\', or \'inline\'.')
	sl.append('#texinfo_show_urls = \'footnote\'\n')

	sl.append('# If true, do not generate a @detailmenu in the "Top" node\'s menu.')
	sl.append('#texinfo_no_detailmenu = False')

	ofh = open("conf.py","w")
	ofh.write("\n".join(sl)+"\n")
	ofh.close()

def make_bat():
	sl = []
	sl.append('@ECHO OFF\n')

	sl.append('REM Command file for Sphinx documentation\n')

	sl.append('if "%SPHINXBUILD%" == "" (')
	sl.append('	set SPHINXBUILD=sphinx-build')
	sl.append(')')
	sl.append('set BUILDDIR=_build')
	sl.append('set ALLSPHINXOPTS=-d %sBUILDDIR%s/doctrees %sSPHINXOPTS%s .' % ('%','%','%','%'))
	sl.append('set I18NSPHINXOPTS=%sSPHINXOPTS%s .' % ('%','%'))
	sl.append('if NOT "%sPAPER%s" == "" (' % ('%','%'))
	sl.append('	set ALLSPHINXOPTS=-D latex_paper_size=%sPAPER%s %sALLSPHINXOPTS%s' % ('%','%','%','%'))
	sl.append('	set I18NSPHINXOPTS=-D latex_paper_size=%sPAPER%s %sI18NSPHINXOPTS%s' % ('%','%','%','%'))
	sl.append(')\n\n')

	sl.append('if "%s1" == "" goto help\n' % '%')

	sl.append('if "%s1" == "help" (' '%')
	sl.append('	:help')
	sl.append('	echo.Please use `make ^<target^>` where ^<target^> is one of')
	sl.append('	echo.  html       to make standalone HTML files')
	sl.append('	echo.  dirhtml    to make HTML files named index.html in directories')
	sl.append('	echo.  singlehtml to make a single large HTML file')
	sl.append('	echo.  pickle     to make pickle files')
	sl.append('	echo.  json       to make JSON files')
	sl.append('	echo.  htmlhelp   to make HTML files and a HTML help project')
	sl.append('	echo.  qthelp     to make HTML files and a qthelp project')
	sl.append('	echo.  devhelp    to make HTML files and a Devhelp project')
	sl.append('	echo.  epub       to make an epub')
	sl.append('	echo.  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter')
	sl.append('	echo.  text       to make text files')
	sl.append('	echo.  man        to make manual pages')
	sl.append('	echo.  texinfo    to make Texinfo files')
	sl.append('	echo.  gettext    to make PO message catalogs')
	sl.append('	echo.  changes    to make an overview over all changed/added/deprecated items')
	sl.append('	echo.  xml        to make Docutils-native XML files')
	sl.append('	echo.  pseudoxml  to make pseudoxml-XML files for display purposes')
	sl.append('	echo.  linkcheck  to check all external links for integrity')
	sl.append('	echo.  doctest    to run all doctests embedded in the documentation if enabled')
	sl.append('	goto end')
	sl.append('\n)')

	sl.append('if "%s1" == "clean" (' % '%')
	sl.append('	for /d %s%si in (%sBUILDDIR%s\*) do rmdir /q /s %s%si' % ('%','%','%','%','%','%'))
	sl.append('	del /q /s %sBUILDDIR%s\*' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n\n')


	sl.append('%sSPHINXBUILD%s 2> nul' % ('%','%'))
	sl.append('if errorlevel 9009 (')
	sl.append('	echo.')
	sl.append('	echo.The \'sphinx-build\' command was not found. Make sure you have Sphinx')
	sl.append('	echo.installed, then set the SPHINXBUILD environment variable to point')
	sl.append('	echo.to the full path of the \'sphinx-build\' executable. Alternatively you')
	sl.append('	echo.may add the Sphinx directory to PATH.')
	sl.append('	echo.')
	sl.append('	echo.If you don\'t have Sphinx installed, grab it from')
	sl.append('	echo.http://sphinx-doc.org/')
	sl.append('	exit /b 1')
	sl.append(')\n')

	sl.append('if "%s1" == "html" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b html %sALLSPHINXOPTS%s %sBUILDDIR%s/html' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished. The HTML pages are in %sBUILDDIR%s/html.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "dirhtml" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b dirhtml %sALLSPHINXOPTS%s %sBUILDDIR%s/dirhtml' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished. The HTML pages are in %sBUILDDIR%s/dirhtml.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "singlehtml" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b singlehtml %sALLSPHINXOPTS%s %sBUILDDIR%s/singlehtml' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished. The HTML pages are in %sBUILDDIR%s/singlehtml.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "pickle" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b pickle %sALLSPHINXOPTS%s %sBUILDDIR%s/pickle' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished; now you can process the pickle files.')
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "json" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b json %sALLSPHINXOPTS%s %sBUILDDIR%s/json' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished; now you can process the JSON files.')
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "htmlhelp" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b htmlhelp %sALLSPHINXOPTS%s %sBUILDDIR%s/htmlhelp' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished; now you can run HTML Help Workshop with the ^')
	sl.append('.hhp project file in %sBUILDDIR%s/htmlhelp.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "qthelp" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b qthelp %sALLSPHINXOPTS%s %sBUILDDIR%s/qthelp' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished; now you can run "qcollectiongenerator" with the ^')
	sl.append('.qhcp project file in %sBUILDDIR%s/qthelp, like this:' % ('%','%'))
	sl.append('	echo.^> qcollectiongenerator %sBUILDDIR%s\qthelp\Test.qhcp' % ('%','%'))
	sl.append('	echo.To view the help file:')
	sl.append('	echo.^> assistant -collectionFile %sBUILDDIR%s\qthelp\Test.ghc' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "devhelp" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b devhelp %sALLSPHINXOPTS%s %sBUILDDIR%s/devhelp' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished.')
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "epub" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b epub %sALLSPHINXOPTS%s %sBUILDDIR%s/epub' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished. The epub file is in %sBUILDDIR%s/epub.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "latex" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b latex %sALLSPHINXOPTS%s %sBUILDDIR%s/latex' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished; the LaTeX files are in %sBUILDDIR%s/latex.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "latexpdf" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b latex %sALLSPHINXOPTS%s %sBUILDDIR%s/latex' % ('%','%','%','%','%','%'))
	sl.append('	cd %sBUILDDIR%s/latex' % ('%','%'))
	sl.append('	make all-pdf')
	sl.append('	cd %sBUILDDIR%s/..' % ('%','%'))
	sl.append('	echo.')
	sl.append('	echo.Build finished; the PDF files are in %sBUILDDIR%s/latex.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "latexpdfja" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b latex %sALLSPHINXOPTS%s %sBUILDDIR%s/latex' % ('%','%','%','%','%','%'))
	sl.append('	cd %sBUILDDIR%s/latex' % ('%','%'))
	sl.append('	make all-pdf-ja')
	sl.append('	cd %sBUILDDIR%s/..' % ('%','%'))
	sl.append('	echo.')
	sl.append('	echo.Build finished; the PDF files are in %sBUILDDIR%s/latex.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "text" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b text %sALLSPHINXOPTS%s %sBUILDDIR%s/text' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished. The text files are in %sBUILDDIR%s/text.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "man" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b man %sALLSPHINXOPTS%s %sBUILDDIR%s/man' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished. The manual pages are in %sBUILDDIR%s/man.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "texinfo" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b texinfo %sALLSPHINXOPTS%s %sBUILDDIR%s/texinfo' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished. The Texinfo files are in %sBUILDDIR%s/texinfo.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "gettext" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b gettext %sI18NSPHINXOPTS%s %sBUILDDIR%s/locale' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished. The message catalogs are in %sBUILDDIR%s/locale.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "changes" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b changes %sALLSPHINXOPTS%s %sBUILDDIR%s/changes' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.The overview file is in %sBUILDDIR%s/changes.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "linkcheck" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b linkcheck %sALLSPHINXOPTS%s %sBUILDDIR%s/linkcheck' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Link check complete; look for any errors in the above output ^')
	sl.append('or in %sBUILDDIR%s/linkcheck/output.txt.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "doctest" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b doctest %sALLSPHINXOPTS%s %sBUILDDIR%s/doctest' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Testing of doctests in the sources finished, look at the ^')
	sl.append('results in %sBUILDDIR%s/doctest/output.txt.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "xml" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b xml %sALLSPHINXOPTS%s %sBUILDDIR%s/xml' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished. The XML files are in %sBUILDDIR%s/xml.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append('if "%s1" == "pseudoxml" (' % '%')
	sl.append('	%sSPHINXBUILD%s -b pseudoxml %sALLSPHINXOPTS%s %sBUILDDIR%s/pseudoxml' % ('%','%','%','%','%','%'))
	sl.append('	if errorlevel 1 exit /b 1')
	sl.append('	echo.')
	sl.append('	echo.Build finished. The pseudo-XML files are in %sBUILDDIR%s/pseudoxml.' % ('%','%'))
	sl.append('	goto end')
	sl.append(')\n')

	sl.append(':end')

	ofh = open("make.bat","w")
	ofh.write("\n".join(sl)+"\n")
	ofh.close()

def make_file():
	sl = []
	sl.append('# Makefile for Sphinx documentation')
	sl.append('#\n')

	sl.append('# You can set these variables from the command line.')
	sl.append('SPHINXOPTS    =')
	sl.append('SPHINXBUILD   = sphinx-build')
	sl.append('PAPER         =')
	sl.append('BUILDDIR      = _build\n')

	sl.append('# User-friendly check for sphinx-build')
	sl.append('ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)')
	sl.append('$(error The \'$(SPHINXBUILD)\' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the \'$(SPHINXBUILD)\' executable. Alternatively you can add the directory with the executable to your PATH. If you don\'t have Sphinx installed, grab it from http://sphinx-doc.org/)')
	sl.append('endif\n')

	sl.append('# Internal variables.')
	sl.append('PAPEROPT_a4     = -D latex_paper_size=a4')
	sl.append('PAPEROPT_letter = -D latex_paper_size=letter')
	sl.append('ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .')
	sl.append('# the i18n builder cannot share the environment and doctrees with the others')
	sl.append('I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .\n')

	sl.append('.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest gettext\n')

	sl.append('help:')
	sl.append('	@echo "Please use \`make <target>\' where <target> is one of"')
	sl.append('	@echo "  html       to make standalone HTML files"')
	sl.append('	@echo "  dirhtml    to make HTML files named index.html in directories"')
	sl.append('	@echo "  singlehtml to make a single large HTML file"')
	sl.append('	@echo "  pickle     to make pickle files"')
	sl.append('	@echo "  json       to make JSON files"')
	sl.append('	@echo "  htmlhelp   to make HTML files and a HTML help project"')
	sl.append('	@echo "  qthelp     to make HTML files and a qthelp project"')
	sl.append('	@echo "  devhelp    to make HTML files and a Devhelp project"')
	sl.append('	@echo "  epub       to make an epub"')
	sl.append('	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"')
	sl.append('	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"')
	sl.append('	@echo "  latexpdfja to make LaTeX files and run them through platex/dvipdfmx"')
	sl.append('	@echo "  text       to make text files"')
	sl.append('	@echo "  man        to make manual pages"')
	sl.append('	@echo "  texinfo    to make Texinfo files"')
	sl.append('	@echo "  info       to make Texinfo files and run them through makeinfo"')
	sl.append('	@echo "  gettext    to make PO message catalogs"')
	sl.append('	@echo "  changes    to make an overview of all changed/added/deprecated items"')
	sl.append('	@echo "  xml        to make Docutils-native XML files"')
	sl.append('	@echo "  pseudoxml  to make pseudoxml-XML files for display purposes"')
	sl.append('	@echo "  linkcheck  to check all external links for integrity"')
	sl.append('	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"\n')

	sl.append('clean:')
	sl.append('	rm -rf $(BUILDDIR)/*\n')

	sl.append('html:')
	sl.append('	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html')
	sl.append('	@echo')
	sl.append('	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."\n')

	sl.append('dirhtml:')
	sl.append('	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml')
	sl.append('	@echo')
	sl.append('	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."\n')

	sl.append('singlehtml:')
	sl.append('	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml')
	sl.append('	@echo')
	sl.append('	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."\n')

	sl.append('pickle:')
	sl.append('	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle')
	sl.append('	@echo')
	sl.append('	@echo "Build finished; now you can process the pickle files."\n')

	sl.append('json:')
	sl.append('	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json')
	sl.append('	@echo')
	sl.append('	@echo "Build finished; now you can process the JSON files."\n')

	sl.append('htmlhelp:')
	sl.append('	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp')
	sl.append('	@echo')
	sl.append('	@echo "Build finished; now you can run HTML Help Workshop with the" \\')
	sl.append('	      ".hhp project file in $(BUILDDIR)/htmlhelp."\n')

	sl.append('qthelp:')
	sl.append('	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp')
	sl.append('	@echo')
	sl.append('	@echo "Build finished; now you can run "qcollectiongenerator" with the" \\')
	sl.append('	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"')
	sl.append('	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/Test.qhcp"')
	sl.append('	@echo "To view the help file:"')
	sl.append('	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/Test.qhc"\n')

	sl.append('devhelp:')
	sl.append('	$(SPHINXBUILD) -b devhelp $(ALLSPHINXOPTS) $(BUILDDIR)/devhelp')
	sl.append('	@echo')
	sl.append('	@echo "Build finished."')
	sl.append('	@echo "To view the help file:"')
	sl.append('	@echo "# mkdir -p $$HOME/.local/share/devhelp/Test"')
	sl.append('	@echo "# ln -s $(BUILDDIR)/devhelp $$HOME/.local/share/devhelp/Test"')
	sl.append('	@echo "# devhelp"\n')

	sl.append('epub:')
	sl.append('	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub')
	sl.append('	@echo')
	sl.append('	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."\n')

	sl.append('latex:')
	sl.append('	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex')
	sl.append('	@echo')
	sl.append('	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."')
	sl.append('	@echo "Run \`make\' in that directory to run these through (pdf)latex" \\')
	sl.append('	      "(use \`make latexpdf\' here to do that automatically)."\n')

	sl.append('latexpdf:')
	sl.append('	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex')
	sl.append('	@echo "Running LaTeX files through pdflatex..."')
	sl.append('	$(MAKE) -C $(BUILDDIR)/latex all-pdf')
	sl.append('	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."\n')

	sl.append('latexpdfja:')
	sl.append('	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex')
	sl.append('	@echo "Running LaTeX files through platex and dvipdfmx..."')
	sl.append('	$(MAKE) -C $(BUILDDIR)/latex all-pdf-ja')
	sl.append('	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."\n')

	sl.append('text:')
	sl.append('	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text')
	sl.append('	@echo')
	sl.append('	@echo "Build finished. The text files are in $(BUILDDIR)/text."\n')

	sl.append('man:')
	sl.append('	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man')
	sl.append('	@echo')
	sl.append('	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."\n')

	sl.append('texinfo:')
	sl.append('	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo')
	sl.append('	@echo')
	sl.append('	@echo "Build finished. The Texinfo files are in $(BUILDDIR)/texinfo."')
	sl.append('	@echo "Run \`make\' in that directory to run these through makeinfo" \\')
	sl.append('	      "(use \`make info\' here to do that automatically)."\n')

	sl.append('info:')
	sl.append('	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo')
	sl.append('	@echo "Running Texinfo files through makeinfo..."')
	sl.append('	make -C $(BUILDDIR)/texinfo info')
	sl.append('	@echo "makeinfo finished; the Info files are in $(BUILDDIR)/texinfo."\n')

	sl.append('gettext:')
	sl.append('	$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(BUILDDIR)/locale')
	sl.append('	@echo')
	sl.append('	@echo "Build finished. The message catalogs are in $(BUILDDIR)/locale."\n')

	sl.append('changes:')
	sl.append('	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes')
	sl.append('	@echo')
	sl.append('	@echo "The overview file is in $(BUILDDIR)/changes."\n')

	sl.append('linkcheck:')
	sl.append('	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck')
	sl.append('	@echo')
	sl.append('	@echo "Link check complete; look for any errors in the above output " \\')
	sl.append('	      "or in $(BUILDDIR)/linkcheck/output.txt."\n')

	sl.append('doctest:')
	sl.append('	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest')
	sl.append('	@echo "Testing of doctests in the sources finished, look at the " \\')
	sl.append('	      "results in $(BUILDDIR)/doctest/output.txt."\n')

	sl.append('xml:')
	sl.append('	$(SPHINXBUILD) -b xml $(ALLSPHINXOPTS) $(BUILDDIR)/xml')
	sl.append('	@echo')
	sl.append('	@echo "Build finished. The XML files are in $(BUILDDIR)/xml."\n')

	sl.append('pseudoxml:')
	sl.append('	$(SPHINXBUILD) -b pseudoxml $(ALLSPHINXOPTS) $(BUILDDIR)/pseudoxml')
	sl.append('	@echo')
	sl.append('	@echo "Build finished. The pseudo-XML files are in $(BUILDDIR)/pseudoxml."\n')

	ofh = open("Makefile","w")
	ofh.write("\n".join(sl)+"\n")
	ofh.close()