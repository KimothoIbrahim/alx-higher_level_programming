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

    def area(self):
        """work out rectangle area"""
        # raise Exception("area() is not implemented")

        return self.__width * self.__height

    def __str__(self):
        """string representation of the rectangle"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
