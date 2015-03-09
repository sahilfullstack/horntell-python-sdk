import json
import horntell
from horntell.http import http_client
from horntell.error import (error, authentication_error, forbidden_error, invalid_request_error, network_error, notfound_error, service_error)

class APIRequestor(object):
    def __init__(self):
        self.client = http_client.RequestsClient()
        self.api_key = horntell.api_key
        self.api_secret = horntell.api_secret
        self.base_url = horntell.base_url


    #
    # Manages all the processing of the request
    #
    # accepts method of the request
    # accepts endpoint to be request
    # accepts parameters to be send with request
    #
    def request(self, method, endpoint, params=None):
        #
        # creating an request
        #
        body, code = self.request_raw(
            method, endpoint, params)
        #
        # interpreting response
        #
        resp = self.interpret_response(body, code)
        return resp

    #
    # Handling all the errors from api
    #
    # accepts body of the error
    # accepts status code of the error
    # accepts response
    #
    def handle_api_error(self, body, code, resp):
        try:
            err = resp['error']
        except (KeyError, TypeError):
            raise error.HorntellError(
                "Invalid response object from API: %r (HTTP response code "
                "was %d)" % (body, code),
                body, code, resp)
        if code == 400:
            raise invalid_request_error.InvalidRequestError(
                err.get('message'), body, code, resp)
        elif code == 401:
            raise authentication_error.AuthenticationError(
                err.get('message'), body, code, resp)
        elif code == 403:
            raise forbidden_error.ForbiddenError(
                err.get('message'), body, code, resp)
        elif code == 404:
            raise notfound_error.NotFoundError(
                err.get('message'), body, code, resp)
        elif code == 500:
            raise service_error.ServiceError(
                err.get('message'), body, code, resp)
        else:
            raise error.HorntellError(err.get('message'), body, code, resp)

    #
    # Handles the requset to be send
    #
    # accepts method of the request
    # accepts url to be request
    # accepts parameters to be send with request
    #
    def request_raw(self, method, endpoint, params=None):

        auth = (self.api_key, self.api_secret)
        url = self.base_url + endpoint

        headers = {
            'Accept': 'application/vnd.horntell.v1+json',
            'Content-Type' : 'application/json'
        }

        #
        # encoding the parameters
        #
        params = json.dumps(params)

        body, code = self.client.request(
            method, url, headers, auth, params)

        return body, code

    #
    # Interprets the response
    #
    # accepts body of the request
    # accepts status code of the request
    #
    def interpret_response(self, body, code):
        #
        # Decodes the response
        #
        try:
            if hasattr(body, 'decode'):
                body = body.decode('utf-8')
            resp = json.loads(body)
        except Exception, e:
            raise error.HorntellError(
                "Invalid response body from API: %s "
                "(HTTP response code was %d)" % (body, code),
                body, code)

        #
        # Handles the exception thrown from api
        #
        if not (200 <= code < 300):
            self.handle_api_error(body, code, resp)

        return resp

