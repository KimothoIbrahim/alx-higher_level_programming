#!/usr/bin/python3
"""Defines a lookup function for object attributes"""


def lookup(obj):
    """"return list of attribs"""
    return (dir(obj))
