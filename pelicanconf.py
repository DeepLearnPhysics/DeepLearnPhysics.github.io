#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'drinkingkazu'
SITENAME = u'DeepLearnPhysics'
GITHUBURL = 'http://github.com/DeepLearnPhysics'
CONTACT = 'mailto:contact@deeplearnphysics.org'
SITEURL = 'http://deeplearnphysics.org'
BLOGURL = SITEURL + '/Blog'
DATAURL = SITEURL + '/DataChallenge'
#SITEURL = '' #uncomment for local development
PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

# Theme
#THEME = 'Flex'
THEME = 'theme'

# Plugins
PLUGINS = ['plugins.keyboard.kb','plugins.render_math']

# Scripts
SCRIPTS = ['https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js','main.js']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
