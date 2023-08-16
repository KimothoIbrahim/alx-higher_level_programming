#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
        list1 = list(a_dictionary.keys())
            list1.sort()
                for x in list1:
                            print("{}: {}".format(x, a_dictionary.get(x)))

