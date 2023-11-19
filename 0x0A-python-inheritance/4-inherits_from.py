#!/usr/bin/python3
"""Module checks if object is a subclass"""


def inherits_from(obj, a_class):
    """func to check if obj is a subclass of a_class

    Args
        obj:
        a_class:

    Return
        True or False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
