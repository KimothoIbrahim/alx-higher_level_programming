#!/usr/bin/python3
"""posts a request and prints response body"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    vals = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(vals)
    data = data.encode('ascii')

    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode('utf-8'))
