import os
import sys
import textwrap
import requests
import horntell

from horntell import error

class RequestsClient:
    name = 'requests'

    def __init__(self):
        self.api_key = horntell.api_key
        self.api_secret = horntell.api_secret
        self.base_url = horntell.base_url

    def request(self, method, endpoint, post_data=None):

        auth = (self.api_key, self.api_secret)
        url = self.base_url + endpoint


        headers = {
            'Accept': 'application/vnd.horntell.v1+json',
            'Content-Type' : 'application/x-www-form-urlencoded'
        }

        try:
            try:
                result = requests.request(method,
                                          url,
                                          headers=headers,
                                          data=post_data,
                                          auth=auth,
                                          timeout=80)

            except TypeError, e:
                raise TypeError(
                    'Warning: It looks like your installed version of the '
                    '"requests" library is not compatible with horntell\'s '
                    'usage thereof. (HINT: The most likely cause is that '
                    'your "requests" library is out of date. You can fix '
                    'that by running "pip install -U requests".) The '
                    'underlying error was: %s' % (e,))

            # This causes the content to actually be read, which could cause
            # e.g. a socket timeout. TODO: The other fetch methods probably
            # are susceptible to the same and should be updated.
            content = result.content
            status_code = result.status_code
        except Exception, e:
            return e
            # Would catch just requests.exceptions.RequestException, but can
            # also raise ValueError, RuntimeError, etc.
            self._handle_request_error(e)
        return content, status_code

    def _handle_request_error(self, e):
        if isinstance(e, requests.exceptions.RequestException):
            msg = ("Unexpected error communicating with horntell.  "
                   "If this problem persists, let us know at "
                   "support@horntell.com.")
            err = "%s: %s" % (type(e).__name__, str(e))
        else:
            msg = ("Unexpected error communicating with horntell. "
                   "It looks like there's probably a configuration "
                   "issue locally.  If this problem persists, let us "
                   "know at support@horntell.com.")
            err = "A %s was raised" % (type(e).__name__,)
            if str(e):
                err += " with error message %s" % (str(e),)
            else:
                err += " with no error message"
        msg = textwrap.fill(msg) + "\n\n(Network error: %s)" % (err,)
        raise error.APIConnectionError(msg)
