#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Return biggest int"""
    if len(my_list) == 0:
        return (None)

    largest = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]

    return (largest)
