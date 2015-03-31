import horntell
from horntell.http import request

class Activity:

    def __init__(self):
        self.request = request.Request()

    #
    # Creates a activity
    #
    # accepts uid
    # accepts activity
    #
    def create(self, uid, activity):
        return self.request.request(
            'post', '/profiles/' + uid + '/activities', activity)
