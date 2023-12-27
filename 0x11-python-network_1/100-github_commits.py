#!/usr/bin/python3
""" list commit on github api """

if __name__ == "__main__":
    import requests
    import sys

    url = f'https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits'

    r = requests.get(url)
    r = r.json()
    for obj in r:
        print(obj['sha'],':', obj['commit']['author']['name'])
