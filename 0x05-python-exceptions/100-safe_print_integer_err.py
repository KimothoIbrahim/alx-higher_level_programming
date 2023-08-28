#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Prints an integer

    If ValueError message is caught, corresponding
    message is printed to stderr.

    Parameters:
        value: Int to print.

    Returns:
        False - If a TypeError or ValueError
        True - if otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
