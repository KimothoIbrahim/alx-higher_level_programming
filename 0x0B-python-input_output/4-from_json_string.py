#!/usr/bin/python3
"""Deserializes JSON string to an object"""
import json


def from_json_string(my_str):
    """
    function converts the JSON string
    `my_str` back to a python object

    Args:
        my_str (str): given JSON string

    Return:
        desrialized object
    """
    return json.loads(my_str)
