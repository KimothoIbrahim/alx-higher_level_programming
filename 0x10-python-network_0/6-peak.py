#!/usr/bin/python3

def find_peak(list_of_integers):
    arr = sorted(list_of_integers)
    if arr:
        return arr[-1]
