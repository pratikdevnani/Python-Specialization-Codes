import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Calib.html'
outer_count = 0

while outer_count < 7:

    inner_count = 0
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        inner_count = inner_count + 1
        if inner_count != 18:
            continue
        else:
            url = tag.get('href', None)

    outer_count = outer_count + 1

print(re.findall('known_by_(.+)\.', url))
