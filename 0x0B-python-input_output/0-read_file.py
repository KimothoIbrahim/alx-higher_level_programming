#!/usr/bin/python3
"""function that reads and prints a txt file to STDOUT"""


def read_file(filename=""):
    """function

    Args:
        filename (str): name of given file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
