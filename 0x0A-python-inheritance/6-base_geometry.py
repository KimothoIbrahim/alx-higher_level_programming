#!/usr/bin/python3
"""Build empty class"""


class BaseGeometry:
    """empty class"""
    def area(self):
        """function raising an exception"""
        raise Exception("area() is not implemented")
