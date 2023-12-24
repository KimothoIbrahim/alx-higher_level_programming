#!/usr/bin/python3
"""Use json"""

if __name__ == "__main__":
    import sys
    import requests

    data = {'q': ""}

    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}

    try:
        res = requests.post('http://0.0.0.0:5000/search_user', data=data)
        res.raise_for_status()
        r = res.json()

        if r:
            print('[{}] {}'.format(r.get('id'), r.get('name')))
        else:
            print('No result')
    except requests.exceptions.JSONDecodeError, requests.exceptions.HTTPError:
        print('Not a valid JSON')
