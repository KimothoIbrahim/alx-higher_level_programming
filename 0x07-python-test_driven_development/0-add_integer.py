#!/usr/bin/python3
"""Adds two numbers (integer or float)"""


def add_integer(a, b=98):
    """
    Adds two numbers of type int or float and returns their sum

    Args:
        a (int, float): first number to add
        b (int , float): second nummber to add

    Returns:
        sum of a and b
    """
    
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)
    
    return (a+b)
