#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    direct = a_dictionary.copy()
    keys = list(direct.keys())

    for x in keys:
        direct[x] *= 2

    return (direct)
