#!/usr/bin/python3
"""Class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is same as class.

    Args:
        obj (any): Object to check.
        a_class (type): The class.
    Returns:
        True or False.
    """
    if type(obj) == a_class:
        return True
    return False
