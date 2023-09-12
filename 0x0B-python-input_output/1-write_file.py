#!/usr/bin/python3
"""Writing to files"""


def write_file(filename="", text=""):
    """Write to text file

    Args:
        filename (str): File to be written
        text (str): text to write in file
    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
