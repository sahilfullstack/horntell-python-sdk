import json

class Response:


    def __init__(self, response):
        self.response = response
        self.body = json.loads(self.response.content)

    #
    #  Returns the orignal response
    #
    def getOriginal(self):
        return self.response

    #
    #  Gets the parsed JSON body
    #
    #  @return array|null (Null in case of No Content)
    #
    def getBody(self):
        return self.body

    #
    #   Gets the HTTP Status Code
    #
    #   @return number
    #
    def getStatusCode(self):
        return self.response.status_code
