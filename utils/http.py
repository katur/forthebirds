"""Utility module with helpers for HTTP response querying."""

import urllib2
import re
from django.core.urlresolvers import reverse


def http_response_url(url):
    """
    If a url responds with "ok" HTTP status, return the response url.
    Otherwise, return None.
    """
    try:
        # Workaround so it doesn't seem like we are a content-stealing bot
        # (we're not! we're just checking if the URL works!)
        url = url.encode('utf8')
        req = urllib2.Request(url, headers={'User-Agent': 'Magic Browser'})
        r = urllib2.urlopen(req)
    except urllib2.URLError as e:
        return None
    except:
        return None

    if r.getcode() == 200:
        return r.url
    else:
        return None


def http_response_ok(url):
    try:
        url = url.encode('utf8')
        r = urllib2.urlopen(url)
    except urllib2.URLError:
        return False
    except:
        return False

    return r.code == 200


def https_to_http(url):
    return re.sub(r'^https', 'http', url)
