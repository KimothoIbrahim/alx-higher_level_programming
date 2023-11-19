#!/usr/bin/python3
"""Test is object is of a specific type """


def is_same_class(obj, a_class):
    """function tests if `obj` is of class `a_class`"""
    if (type(obj) == a_class):
        return True
    else:
        return False
