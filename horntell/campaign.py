import horntell
from horntell.http import http_client

class Campaign:

	def __init__(self):
		self.client = http_client.RequestsClient()

	#
    # Trigger campaign for a profile
    #
    # accepts uid
    # accepts campaignId
    #
	def toProfile(self, uid, campaignId):
		return self.client.request(
			'post', '/profiles/' + uid + '/campaigns/' + campaignId)

	#
    # Trigger campaign to multiple profiles
    #
    # accepts array of profiles
    # accepts campaignId
    #
	def toProfiles(self, profiles, campaignId):
		profiles = {'profile_uids[]' : profiles }

		return self.client.request(
			'post', '/profiles/campaigns/' + campaignId, profiles)
