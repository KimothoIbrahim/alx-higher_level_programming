#!/usr/bin/python3
"""get data for given url"""

if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as res:
        info = res.info()

        print(info['X-Request-Id'])
