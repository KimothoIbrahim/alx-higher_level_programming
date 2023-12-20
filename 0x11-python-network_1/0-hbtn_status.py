#!/usr/bin/python3
""" The script fetches a url using urllib module"""

import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    res = response.read()

print('Body response:')
print(' - type: {} '.format(type(res)))
print(' - content: {} '.format(res))
print(' - utf8 content: {} '.format(res.decode('utf-8')))
