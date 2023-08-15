#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """MUL"""
    times = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            times.append(True)
        else:
            times.append(False)

    return (times)
