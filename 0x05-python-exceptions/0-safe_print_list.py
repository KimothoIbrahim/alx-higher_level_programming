#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print from a list

    parameters:
        my_list : a list of all emements
        x: how many elements to print.

    Returns:
        Number of printed elements.
    """
    numy = 0
    for t in range(x):
        try:
            print("{}".format(my_list[t]), end="")
            numy += 1
        except IndexError:
            break
    print("")
    return (numy)
