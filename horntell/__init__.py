
api_key = None
api_secret = None

base_url = 'http://api.horntell.com'
verify_ssl_certs = True

#sdk
from horntell.profile import Profile
from horntell.horn import Horn
from horntell.campaign import Campaign
from horntell.activity import Activity

from horntell.error.invalid_request_error import InvalidRequestError
from horntell.error.authentication_error import AuthenticationError
from horntell.error.forbidden_error import ForbiddenError
from horntell.error.network_error import NetworkError
from horntell.error.notfound_error import NotFoundError
from horntell.error.service_error import ServiceError
from horntell.error.error import HorntellError

# from horntell.error import (error, authentication_error, forbidden_error, invalid_request_error, network_error, notfound_error, service_error)
