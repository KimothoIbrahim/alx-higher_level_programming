#!/usr/bin/python3
"""creating an object from JSON file"""
import json


def load_from_json_file(filename):
    """
    function retreaves and object from the JSON file "filename"

    Args:
        filename (str): JSON file to retreave object from

    Return:
        deserialized object
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
