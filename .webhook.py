#!/usr/bin/env python
import sys, urllib2, json

# print('Content-type: json\n')
print('<title>Hello World</title>')
print("yes")

f = open("webhook.txt", 'a')
# os.getenv("QUERY_STRING")
payload = sys.stdin.read()
obj = urllib2.unquote(payload)
output = json.loads(obj.split('=')[1])
f.write(output['id'])
# f.write(obj.split('='));
# # f.write(obj)
# f.write(e['id'])
# f.write(son1[1]))
# form = cgi.FieldStorage(true)
# f.write(form.getValue("horntell_event"));
# f.write(web.input())
# f.write(web.input('horntell_event'))
# f.write(web.data('horntell_event'))
# f.write(request.get('horntell_event'))
f.close()

