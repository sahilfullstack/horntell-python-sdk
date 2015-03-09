import horntell
from horntell.http import api_requester

class Profile:

    def __init__(self):
        self.requester = api_requester.APIRequestor()

    #
    # Returns a profile
    #
    # accepts uid
    #
    def find(self, uid):
        return self.requester.request(
            'get', '/profiles/' + uid)
    #
    # Creates a profile
    #
    def create(self, profile=None):
        return self.requester.request(
            'post', '/profiles', profile)

    #
    # Updates a profile
    #
    def update(self, uid, profile=None):
        return self.requester.request(
            'put', '/profiles/' + uid, profile)
    #
    # Deletes a profile
    #
    # accepts uid
    #
    def delete(self, uid):
        return self.requester.request(
            'delete', '/profiles/' + uid)
