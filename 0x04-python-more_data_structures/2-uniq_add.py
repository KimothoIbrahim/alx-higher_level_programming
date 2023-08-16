#!/usr/bin/python3
def uniq_add(my_list=[]):
    list1 = set(my_list)
    number = 0

    for i in list1:
        number += i
    return (number)
