#!/usr/bin/python3
"""represent a give object in JSON"""
import json


def to_json_string(my_obj):
    """return the JSON representation of `my_obj`

    Args:
        my_obj (object): the object to represent as a JSON string

    Return:
        JSON string representaion
    """
    return json.dumps(my_obj)
