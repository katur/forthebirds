"""Utility module with helpers for HTTP response querying."""

import urllib2
from django.core.urlresolvers import reverse


def http_response_url(url):
    """
    If a url responds with "ok" HTTP status, return the response url.
    Otherwise, return None.
    """
    try:
        # Workaround so it doesn't seem like we are a content-stealing bot
        # (we're not! we're just checking if the URL works!)
        req = urllib2.Request(url, headers={'User-Agent': 'Magic Browser'})
        r = urllib2.urlopen(req)
    except urllib2.URLError as e:
        return None

    if r.code == 200:
        return r.url
    else:
        return None
