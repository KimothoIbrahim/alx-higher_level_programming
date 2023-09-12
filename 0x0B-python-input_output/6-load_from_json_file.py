#!/usr/bin/python3
"""using file to make Json objects"""
import json


def load_from_json_file(filename):
    """make a json from file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
