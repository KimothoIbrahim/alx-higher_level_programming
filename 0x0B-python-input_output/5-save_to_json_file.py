#!/usr/bin/python3
"""Saving Json representations to files"""
import json


def save_to_json_file(my_obj, filename):
    """save to text file as json"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dumps(my_obj, f)
