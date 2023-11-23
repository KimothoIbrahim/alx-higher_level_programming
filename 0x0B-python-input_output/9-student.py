#!/usr/bin/python3
"""defines a Class"""


class Student:

    def __init__(self, first_name, last_name, age):
        """initialize a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
