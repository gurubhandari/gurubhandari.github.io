# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Guru Bhandari'
copyright = '2022, Guru Prasad Bhandari'
author = 'Guru Prasad Bhandari'

release = '0.1'
version = 'Biodata'

# -- General configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# html_theme = 'sphinx_rtd_theme'
html_theme = 'alabaster'

html_favicon = 'HK-logo.png'

html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'


# html theme options for alabaster
html_theme_options = {
    'logo': 'HK-logo.png',
    'logo_name': 'false',
    'github_user': 'gurubhandari',
    'github_repo': 'website',
    'fixed_sidebar': 'false',
    # 'description': description,
    'badge_branch': 'master',
    'github_banner': 'false',
    'github_button': 'false',
    'travis_button': 'false',
    'show_powered_by': 'true',
    'show_relbar_bottom': 'true',
    'extra_nav_links': {
        'GitHub/gurubhandari': 'https://github.com/gurubhandari',
        'LinkedIn/gurubhandari': 'https://www.linkedin.com/in/gurubhandari/'
    }
}