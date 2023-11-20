#!/usr/bin/python3
"""Build empty class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """inheriting class"""

    def __init__(self, width, height):
        """Initialize a new rectangle

        args:
            width (int):Rectangle width
            height (int): Rectngle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
