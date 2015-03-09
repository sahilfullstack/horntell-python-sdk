from horntell.error.error import HorntellError

class NetworkError(HorntellError):
    def __init__(self, message=None, code=None, type=None):
	    super(NetworkError, self).__init__(message, code, type)
	    self.message="Could not connect to Horntell. Please check your network connection and try again. If the problem persists, please get in touch with us at hello@horntell.com."
	    self.type='network_error'