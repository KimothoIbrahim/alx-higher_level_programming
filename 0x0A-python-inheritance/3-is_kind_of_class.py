#!/usr/bin/python3
"""Class-checking function."""


def is_kind_of_class(obj, a_class):
    """See if instance or inherited instance of some class.

    Args:
        obj (any): Object to check.
        a_class (type): The class.
    Returns:
        True or False.
    """
    if isinstance(obj, a_class):
        return True
    return False
