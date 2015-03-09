import horntell
from horntell.http import api_requester

class Activity:

    def __init__(self):
        self.requester = api_requester.APIRequestor()

    #
    # Creates a activity
    #
    # accepts uid
    # accepts activity
    #
    def create(self, uid, activity):
        return self.requester.request(
            'post', '/profiles/' + uid + '/activities', activity)
