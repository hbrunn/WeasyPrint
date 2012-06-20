# coding: utf8
"""
    weasyprint.compat
    -----------------

    Workarounds for compatibility with Python 2 and 3 in the same code base.

    :copyright: Copyright 2011-2012 Simon Sapin and contributors, see AUTHORS.
    :license: BSD, see LICENSE for details.

"""

from __future__ import division, unicode_literals

import sys
import email


if sys.version_info[0] >= 3:
    # Python 3
    from urllib.parse import (
        urljoin, urlsplit, quote, unquote, unquote_to_bytes)
    from urllib.request import urlopen, Request, pathname2url
    from array import array

    unicode = str
    basestring = str
    xrange = range
    iteritems = dict.items
    izip = zip


    def urlopen_contenttype(url):
        """Return (file_obj, mime_type, encoding)"""
        result = urlopen(url)
        info = result.info()
        mime_type = info.get_content_type()
        charset = info.get_param('charset')
        return result, mime_type, charset


    def parse_email(data):
        if isinstance(data, bytes):
            data = data.decode('utf8')
        return email.message_from_string(data)


    def ints_from_bytes(byte_string):
        """Return a list of ints from a byte string"""
        return list(byte_string)

else:
    # Python 2
    from urlparse import urljoin, urlsplit
    from urllib2 import urlopen, Request
    from urllib import pathname2url, quote, unquote
    from array import array as _array
    from itertools import izip

    unicode = unicode
    basestring = basestring
    xrange = xrange
    iteritems = dict.iteritems


    def array(typecode, initializer):
        return _array(typecode.encode('ascii'), initializer)


    def urlopen_contenttype(url):
        """Return (file_obj, mime_type, encoding)"""
        result = urlopen(url)
        info = result.info()
        mime_type = info.gettype()
        charset = info.getparam('charset')
        return result, mime_type, charset


    def unquote_to_bytes(data):
        if isinstance(data, unicode):
            data = data.encode('ascii')
        return unquote(data)


    def parse_email(data):
        if isinstance(data, unicode):
            data = data.encode('utf8')
        return email.message_from_string(data)


    def ints_from_bytes(byte_string):
        """Return a list of ints from a byte string"""
        return map(ord, byte_string)
