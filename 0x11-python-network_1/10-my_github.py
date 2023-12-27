#!/usr/bin/python3
""" query github api """

if __name__ == "__main__":

    import sys
    import requests

    auth = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user', auth=auth)

    r = r.json()
    print(r.get('id'))

