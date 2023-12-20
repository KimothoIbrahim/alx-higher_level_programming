#!/usr/bin/python3
""" The script fetches a url using urllib module"""

from urllib.request import urlopen

with urlopen('https://alx-intranet.hbtn.io/status') as response:
    res = response.read()

    print('Body response:')
    print(' - type: {}'.format(type(res)))
    print(' - content: {}'.format(res))
    print(' - utf8 content: {}'.format(res.decode('utf-8')))
