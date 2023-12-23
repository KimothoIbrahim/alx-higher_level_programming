#!/usr/bin/python3
"""Use json"""

if __name__ == "__main__":
    import sys
    import requests

    data = {'q': ""}

    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}

    r = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        r = r.json()
        if r:
            print('', r.get('id'), r.get('name'))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
