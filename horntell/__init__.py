key = None
secret = None

base = 'http://api.horntell.com'
version = 'v1'

#sdk
from horntell.app import App
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
