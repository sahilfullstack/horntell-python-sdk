import horntell

print "Attempting horn..."

horntell.api_key = 'T4BCjNDpWLU2qs1nQO220Chwf8wgbHIEExHoPqVH'
horntell.api_secret = 'Brx4DLKjEWs9aufHpo2sVVznVd1LNZY6S3KiY8E3'
horntell.base_url = 'http://horntell-api.dev'

# resp = horntell.Profile().create({
#             "uid": "470",
#             "first_name": "Sahil",
#             "last_name": "Doe",
#             "email": "john@example.com",
#             "signedup_at": "843478374"
#         })

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

options = {
  "format" : "ask",
  "type" : "success",
  "bubble": 0,
  "text" : "sdsdsdb",
  "options[]" : [[['text', 'type'], ['text', 'type'], ['text', 'type']]]

}

# options['options[]'].append(['text', 'type'])

resp = horntell.Horn().toProfiles(['470', '30992'], options)



# resp = horntell.Activity().create('470', {
#             "name": "Chaman",
#             "revenue": "34",
#             "direction":"inbound"
#         })

print 'Success: %r' % (options, )



