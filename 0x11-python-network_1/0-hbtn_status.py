#!/usr/bin/python3
""" The script fetches a url using urllib module"""

if __name__ == "__main__":
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        res = response.read()

        print('Body response:')
        print(' - type: {}'.format(type(res)))
        print(' - content: {}'.format(res))
        print(' - utf8 content: {}'.format(res.decode('utf-8')))
