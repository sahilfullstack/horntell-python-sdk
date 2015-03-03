import horntell
from horntell.http import http_client

class Activity:

    def __init__(self):
        self.client = http_client.RequestsClient()

    #
    # Creates a activity
    #
    # accepts uid
    # accepts activity
    #
    def create(self, uid, activity):
        return self.client.request(
            'post', '/profiles/' + uid + '/activities', activity)
