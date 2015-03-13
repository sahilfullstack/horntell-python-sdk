import horntell
from horntell.http import api_requester

class Campaign:

	def __init__(self):
		self.requester = api_requester.APIRequestor()

	#
    # Trigger campaign for a profile
    #
    # accepts uid
    # accepts campaignId
    #
	def to_profile(self, uid, campaignId):
		return self.requester.request(
			'post', '/profiles/' + uid + '/campaigns/' + campaignId)

	#
    # Trigger campaign to multiple profiles
    #
    # accepts array of profiles
    # accepts campaignId
    #
	def to_profiles(self, profiles, campaignId):
		profiles = {'profile_uids' : profiles }

		return self.requester.request(
			'post', '/profiles/campaigns/' + campaignId, profiles)
