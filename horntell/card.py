import horntell
from horntell.http import request

class Card:

	def __init__(self):
		self.request = request.Request()

	#
	# Sends card to a profile
	#
	def to_profile(self, uid, card):
		card['canvas'] =  (card['canvas'] if ('canvas' in  card) else 'default');
		return self.request.request(
			'post', '/profiles/' + uid + '/cards', card)
	#
	# Sends card to multiple profiles
	#
	def to_profiles(self, profiles, card):
		card['canvas'] =  (card['canvas'] if ('canvas' in  card) else 'default');
		card['profile_uids'] = profiles

		return self.request.request(
			'post', '/profiles/cards', card)
	#
	# Sends card to a channel
	#
	def to_channel(self, uid, card):
		card['canvas'] =  (card['canvas'] if ('canvas' in  card) else 'default');
		return self.request.request(
			'post', '/channels/' + uid + '/cards', card)
	#
	# Sends card to multiple profiles
	#
	def to_channels(self, profiles, card):
		card['channel_uids'] = profiles
		card['canvas'] =  (card['canvas'] if ('canvas' in  card) else 'default');
		return self.request.request(
			'post', '/channels/cards', card)