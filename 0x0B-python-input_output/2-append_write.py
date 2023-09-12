#!/usr/bin/python3
"""Appending to files in python"""


def append_write(filename="", text=""):
    """Append text to a provided file

    Args:
        filename (str): file to write to
        text (str): text to input to file

    Returns:
        number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
