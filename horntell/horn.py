import horntell
from horntell.http import api_requester

class Horn:

	def __init__(self):
		self.requester = api_requester.APIRequestor()

	#
    # Sends horn to a profile
    #
    # accepts uid
    # accepts horn
    #
	def to_profile(self, uid, horn):
		return self.requester.request(
			'post', '/profiles/' + uid + '/horns', horn)
	#
    # Sends horn to multiple profiles
    #
    # accepts array of profiles
    # accepts horn
    #
	def to_profiles(self, profiles, horn):
		horn['profile_uids'] = profiles

		return self.requester.request(
			'post', '/profiles/horns', horn)
