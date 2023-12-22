#!/usr/bin/python3
"""request http with error checks """

import sys
import urllib.request

try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print('Error code:', e.code)
