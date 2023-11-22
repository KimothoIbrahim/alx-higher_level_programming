#!/usr/bin/python3
"""writes JSON string representaion
of Obj to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """write my_obj's JSON sting representation
    into the txt file 'filename'

    Args:
        my_obj (object): object to convert and save as JSON
        filename (str): file to write the JSON obj in
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
