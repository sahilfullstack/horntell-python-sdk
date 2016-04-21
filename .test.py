import horntell

horntell.App().set_base('http://api.horntell.dev')
horntell.App().init('3TV0xpQLnoqoniaFZu0psXQoqtIPIgvfvKyMoBEZ', 'oe3x2VCMlhHaUsIF2pXSs5nTLYoA8xGPxoD03vve')

resp = horntell.Campaign().to_channels(['default'], '571499ce20ef71c8048b4568')

print resp.get_status_code()

# print result.get_body().get('data')

# print 'Success: %r' % (result.getStatusCode, )

#profile

	# resp = horntell.Profile().create({
 #            "uid": "4709130",
 #            "first_name": "Sahil",
 #            "last_name": "Doe",
 #            "email": "john@example.com",
 #            "signedup_at": 843478374
 #        })
 	# resp = horntell.Profile().find('4709130')
	# print resp

 	# return resp
	# resp = horntell.Profile().update('4709130', {
	#             "first_name": "Chaman",
	#             "last_name": "Doe",
	#             "email": "john@example.com",
	#             "signedup_at": "843478374"
	#         })

	# resp = horntell.Profile().find('470')

#horn
	# options = {
	#   "format" : "ask",
	#   "type" : "success",
	#   "bubble": 0,
	#   "text" : "sdsdsdb",
	#   "options" : [
	# 		{
	# 			"text" : "Yes",
	# 			"type" : "success"
	# 		},
	# 		{
	# 			"text" : "No",
	# 			"type" : "danger"
	# 		},
	# 		{
	# 			"text" : "Chaos",
	# 			"type" : "default"
	# 		}
	# 		]

	# }


	# resp = horntell.Horn().to_profiles(['4709130'], options)
	# resp = horntell.Horn().to_profile('4709130', options)

	#campaign
	# resp = horntell.Campaign().to_profile('4709130', '54f562ded76af12d2d8b4567')
	# resp = horntell.Campaign().to_profiles(['4709130'], '54f562ded76af12d2d8b4567')

	#activity
	# resp = horntell.Activity().create('470', {
	#             "name": "Chaman",
	#             "revenue": "34",
	#             "direction":"inbound"
	#         })
	# print resp.getStatusCode
	# print resp
# 	print 'Success: %r' % (resp.get_body())
# except horntell.errors.InvalidRequestError, e:
# 	print e.message, e.code, e.type
# except horntell.errors.AuthenticationError, e:
# 	print e.message
# except horntell.errors.NotFoundError, e:
# 	print e.message
# except horntell.errors.NetworkError, e:
# 	print e.message, e.type, e.code
# except horntell.errors.Error, e:
# 	print e.message, e.code

# resp = horntell.Profile().find('460')

# resp = horntell.Profile().update('470', {
#             "uid": "470",
#             "first_name": "Chaman",
#             "last_name": "Doe",
#             "email": "john@example.com",
#             "signedup_at": "843478374"
#         })

# resp = horntell.Profile().delete('460')

# resp = horntell.Campaign().toProfiles('470', '54f562ded76af12d2d8b4567')
# resp = horntell.Horn().toProfiles(['470', '30992'], {
#   "format" : "ask",
#   "type" : "success",
#   "bubble": 0,
#   "text" : "sdsdsdb",
#   "options[]" : []

# })
#

# options = {
#   "format" : "ask",
#   "type" : "success",
#   "bubble": 0,
#   "text" : "sdsdsdb",
#   "options" : [
# 		{
# 			"text" : "Yes",
# 			"type" : "success"
# 		},
# 		{
# 			"text" : "No",
# 			"type" : "danger"
# 		},
# 		{
# 			"text" : "Chaos",
# 			"type" : "default"
# 		}
# 		]

# }

# options['options[]'].append(['text', 'type'])

# resp = horntell.Horn().toProfiles(['470', '30992'], options)



# resp = horntell.Activity().create('470', {
#             "name": "Chaman",
#             "revenue": "34",
#             "direction":"inbound"
#         })

# print 'Success: %r' % (resp, )
