#!/usr/bin/python3
""" max int in array"""

def find_peak(list_of_integers):
    """the function"""

    arr = sorted(list_of_integers)
    if arr:
        return arr[-1]
