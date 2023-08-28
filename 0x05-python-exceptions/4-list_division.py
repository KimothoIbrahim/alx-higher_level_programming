#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Division func.

    Parameters:
        my_list_1: First list.
        my_list_2: Second list.
        list_length: How many elements to divide

    Returns:
        new List.
    """
    list0 = []
    for t in range(0, list_length):
        try:
            quo = my_list_1[t] / my_list_2[t]
        except TypeError:
            print("wrong type")
            quo = 0
        except ZeroDivisionError:
            print("division by 0")
            quo = 0
        except IndexError:
            print("out of range")
            quo = 0
        finally:
            list0.append(quo)
    return (list0)
