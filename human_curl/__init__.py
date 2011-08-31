#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
HUMAN cURL LIBRARY
~~~~~~~~~~~~~~~~~~

cURL wrapper for Human

Features:
    - Fast
    - Custom HTTP headers
    - Request data/params
    - Multiple file uploading
    - Cookies support (dict or CookieJar)
    - Redirection history
    - Proxy support (http, https, socks4/5)
    - Custom interface for request!
    - Auto decompression of GZipped content
    - Unicode URL support
    - Request timers and another info
    - Certificate validation
    - ipv6 support

:copyright: (c) 2011 by Alexandr Lispython (alex@obout.ru).
:license: BSD, see LICENSE for more details.
"""

__all__ = ('get', 'put', 'head', 'post', 'delete', 'request', 'options',
           'Request', 'Response', 'get_version')
__author__ = "Alex Lispython (alex@obout.ru)"
__license__ = "BSD, see LICENSE for more details"
__version_info__ = (0, 0, 1)
__version__ = ".".join(map(str, __version_info__))
__maintainer__ = "Alexandr Lispython (alex@obout.ru)"


def get_version():
    return __version__

from .methods import get, put, head, post, delete, request, options
from .core import Request, Response
from .exceptions import CurlError, InterfaceError, InvalidMethod