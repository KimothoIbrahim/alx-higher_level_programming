#!/usr/bin/python3
"""script writes given text to a file"""


def write_file(filename="", text=""):
    """Function write the text `text` to
    the file `filename`

    Args:
        filename (str): name of file to be written
        text (str): content to be written

    Return:
        number of characters written to `filename`
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return (file.write(text))
