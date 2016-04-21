import horntell
import sys, urllib2, json

class Event:

	#
	# return decoded payload from event
	#
	def fromWebhook(self):
		payload = sys.stdin.read()
		decodedPayload = urllib2.unquote(payload)
		return json.loads(decodedPayload.split('horntell_event=')[1])