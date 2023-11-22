#!/usr/bin/python3
"""append text to a file"""


def append_write(filename="", text=""):
    """
    function attaches 'text' to the file `filename`

    Args:
        filename (str): string to a file to be written
        text (str): text to add to the file "filename"
    """

    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
