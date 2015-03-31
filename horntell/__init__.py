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

from horntell.errors.invalid_request_error import InvalidRequestError
from horntell.errors.authentication_error import AuthenticationError
from horntell.errors.forbidden_error import ForbiddenError
from horntell.errors.network_error import NetworkError
from horntell.errors.notfound_error import NotFoundError
from horntell.errors.service_error import ServiceError
from horntell.errors.error import HorntellError

# from horntell.errors import (error, authentication_error, forbidden_error, invalid_request_error, network_error, notfound_error, service_error)
