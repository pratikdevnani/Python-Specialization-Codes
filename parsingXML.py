import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_526517.xml'

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
tree = ET.fromstring(data)

results = tree.findall('.//count')

summ = 0
for node in results:
    summ = summ + int(node.text)

print(summ)
