#!/usr/bin/python3
""" Use requests module """

if __name__ == "__main__":
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type:', type(r.text))
    print('\t- content:', r.text)
