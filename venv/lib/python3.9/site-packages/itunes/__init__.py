# -*- coding: utf-8 -*-
"""A python interface for searching the iTunes Store"""

version_info = (1, 0, 1)
__name__ = 'itunes'
__doc__ = 'A python interface to search iTunes Store'
__author__ = 'Jonathan Nappi'
__version__ = '.'.join([str(i) for i in version_info])
__license__ = 'GPL'
__maintainer__ = 'Jonathan Nappi'
__email__ = 'moogar@comcast.net'
__status__ = 'Stable'

#: iTunes API version
API_VERSION = '2'

#: ISO Country Store
COUNTRY = 'US'

#: iTunes API Hostname
HOST_NAME = 'https://itunes.apple.com/'

try:
    from itunes.base import *  # NOQA
    from itunes.search import *  # NOQA
except ImportError:
    pass  # Assume we're installing if we can't import search functions
