#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer

    Parameters:
        value: Int to Print

    Returns:
        False - If it's a TypeError or ValueError
        True- if otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
