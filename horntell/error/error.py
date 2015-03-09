# Exceptions
class HorntellError(Exception):

    def __init__(self, message=None, code=None,
                 type=None):
        super(HorntellError, self).__init__(message)

        self.code = code
        self.type = type