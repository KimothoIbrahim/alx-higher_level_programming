#!/usr/bin/python3
"""post requests"""

if __name__ == "__main__":
    import sys
    import requests

    data = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=data)

    print(r.text)
