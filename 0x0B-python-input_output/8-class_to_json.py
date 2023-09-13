#!/usr/bin/python3
"""Class-to-JSON function."""


def class_to_json(obj):
    """simple data structure in JSON representation."""
    return obj.__dict__
