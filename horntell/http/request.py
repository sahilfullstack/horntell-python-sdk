import json
import horntell
from horntell.http import client
from horntell.errors import (error, authentication_error, forbidden_error, invalid_request_error, network_error, notfound_error, service_error)
from horntell.http.response import Response

class Request(object):
    def __init__(self):
        self.client = client.Client()
        self.key = horntell.key
        self.secret = horntell.secret
        self.base = horntell.base


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
        result = self.request_raw(
            method, endpoint, params)

        #
        # interpreting response
        #
        response = self.interpret_response(result)

        return Response(response)

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
                "was %d)" % (body, code), code)
        if code == 400:
            raise invalid_request_error.InvalidRequestError(
                err.get('message'), code, err.get('type'))
        elif code == 401:
            raise authentication_error.AuthenticationError(
                err.get('message'), code, err.get('type'))
        elif code == 403:
            raise forbidden_error.ForbiddenError(
                err.get('message'), code, err.get('type'))
        elif code == 404:
            raise notfound_error.NotFoundError(
                err.get('message'), code, err.get('type'))
        elif code == 500:
            raise service_error.ServiceError(
                err.get('message'), code, err.get('type'))
        else:
            raise error.HorntellError(err.get('message'), code, err.get('type'))

    #
    # Handles the requset to be send
    #
    # accepts method of the request
    # accepts url to be request
    # accepts parameters to be send with request
    #
    def request_raw(self, method, endpoint, params=None):

        auth = (self.key, self.secret)
        url = self.base + endpoint

        headers = {
            'Accept': 'application/vnd.horntell.'+ horntell.version +'+json',
            'Content-Type' : 'application/json'
        }

        #
        # encoding the parameters
        #
        params = json.dumps(params)

        return self.client.request(
            method, url, headers, auth, params)

    #
    # Interprets the response
    #
    # accepts body of the request
    # accepts status code of the request
    #
    def interpret_response(self, result):
        body = result.content
        code = result.status_code

        if (code == 204):
            return result

        #
        # Decodes the response
        #
        try:
            if hasattr(body, 'decode'):
                body = body.decode('utf-8')
            resp = json.loads(body)
        except Exception, e:
            return e
            raise error.HorntellError(
                "Invalid response body from API: %s "
                "(HTTP response code was %d)" % (body, code), code)

        #
        # Handles the exception thrown from api
        #
        if not (200 <= code < 300):
            self.handle_api_error(body, code, resp)

        return result

