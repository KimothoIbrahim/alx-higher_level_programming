#!/usr/bin/python3
"""module describes function to print file to STDOUT """


def read_file(filename=""):
    """The function reads a file out to stdout

    Args:
        filename (file): file to read
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
