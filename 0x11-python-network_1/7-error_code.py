#!/usr/bin/python3
"""Use response.OK """

if __name__ == "__main__":
    import sys
    import requests

    r = requests.get(sys.argv[1])

    if r.ok:
        print(r.text)
    else:
        print('Error code:', r.status_code)
