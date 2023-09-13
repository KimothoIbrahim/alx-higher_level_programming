#!/usr/bin/python3
"""Insertion function for text files."""


def append_after(filename="", search_string="", new_string=""):
    """Add text after each line.

    Args:
        filename (str): File name.
        search_string (str): What to search for.
        new_string (str): The string to insert.
    """
    txt = ""
    with open(filename) as f:
        for line in f:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as p:
        p.write(txt)
