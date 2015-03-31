import horntell
from horntell.http import request

class Campaign:

	def __init__(self):
		self.request = request.Request()

	#
    # Trigger campaign for a profile
    #
    # accepts uid
    # accepts campaignId
    #
	def to_profile(self, uid, campaignId):
		return self.request.request(
			'post', '/profiles/' + uid + '/campaigns/' + campaignId)

	#
    # Trigger campaign to multiple profiles
    #
    # accepts array of profiles
    # accepts campaignId
    #
	def to_profiles(self, profiles, campaignId):
		profiles = {'profile_uids' : profiles }

		return self.request.request(
			'post', '/profiles/campaigns/' + campaignId, profiles)
