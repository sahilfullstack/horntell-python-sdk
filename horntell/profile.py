import horntell
from horntell.http import http_client

class Profile:

    def __init__(self):
        self.client = http_client.RequestsClient()

    #
    # Returns a profile
    #
    # accepts uid
    #
    def find(self, uid):
        return self.client.request(
            'get', '/profiles/' + uid)
    #
    # Creates a profile
    #
    def create(self, profile=None):
        return self.client.request(
            'post', '/profiles', profile)

    #
    # Updates a profile
    #
    def update(self, uid, profile=None):
        return self.client.request(
            'put', '/profiles/' + uid, profile)
    #
    # Deletes a profile
    #
    # accepts uid
    #
    def delete(self, uid):
        return self.client.request(
            'delete', '/profiles/' + uid)
