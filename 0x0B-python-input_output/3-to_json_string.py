#!/usr/bin/python3
"""Working with JSON"""
import json


def to_json_string(my_obj):
    """Return json representation of an object

    Args:
        my_obj: given object

    Returns:
        string representstion of object
    """
    return json.dumps(my_obj)
