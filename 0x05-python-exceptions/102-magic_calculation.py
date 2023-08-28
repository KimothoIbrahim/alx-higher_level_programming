#!/usr/bin/python3
    """
    comment section
    """

def magic_calculation(a, b):
    res = 0
    for t in range(1, 3):
        try:
            if t > a:
                raise Exception('Too far')
            else:
                res += a ** b / t
        except:
            res = b + a
            break
    return (res)
