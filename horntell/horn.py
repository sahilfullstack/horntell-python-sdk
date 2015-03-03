import horntell
from horntell.http import http_client

class Horn:

	def __init__(self):
		self.client = http_client.RequestsClient()

	#
    # Sends horn to a profile
    #
    # accepts uid
    # accepts horn
    #
	def toProfile(self, uid, horn):
		return self.client.request(
			'post', '/profiles/' + uid + '/horns', horn)
	#
    # Sends horn to multiple profiles
    #
    # accepts array of profiles
    # accepts horn
    #
	def toProfiles(self, profiles, horn):
		horn['profile_uids[]'] = profiles

		return self.client.request(
			'post', '/profiles/horns', horn)
