import json
import urllib.request, urllib.parse, urllib.error
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter a link:")

uh = urllib.request.urlopen(url, context=ctx)

#decode used for decoding from utf-8 to unicode
data = uh.read().decode()
info = json.loads(data)

#prints the entire json with an indent of 2
print(json.dumps(info, indent = 2))

summ = 0
for item in info["comments"]:
    summ = summ + int(item['count'])

print(summ)
