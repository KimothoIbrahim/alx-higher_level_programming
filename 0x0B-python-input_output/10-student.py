#!/usr/bin/python3
"""defines a Class"""


class Student:

    def __init__(self, first_name, last_name, age):
        """initialize a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        for attr in attrs:
            if type(attr) != str:
                return self.__dict__

        return {attr: self.__dict__[attr] for attr in attrs}
