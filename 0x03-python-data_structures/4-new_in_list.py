#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if (idx < 0) or (idx > len(my_list) - 1):
        return my_list.copy()

    editable_list = my_list.copy()
    editable_list[idx] = element
    return editable_list
