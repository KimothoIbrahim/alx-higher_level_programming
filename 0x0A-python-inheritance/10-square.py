#!/usr/bin/python3
"""module describes a class inheriting from rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class defination"""
    def __init__(self, size):
        """Initializes the square"""
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """calc the Area"""
        return (self.__size * self.__size)
