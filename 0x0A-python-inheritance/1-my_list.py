#!/usr/bin/python3

class MyList(list):
    """print a soted list"""

    def print_sorted(self):
        """prints a sorted list of current list instance"""
        print(sorted(self))
