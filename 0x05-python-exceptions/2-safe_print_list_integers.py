#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integer elements.

    Parameters:
        my_list: print elements fromthis list
        x: The number of elements to be printed

    Returns:
        The number of elements printed.
    """
    numy = 0
    for t in range(0, x):
        try:
            print("{:d}".format(my_list[t]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (numy)
