#!/usr/bin/python3

def safe_print_division(a, b):
    """Divide a by b. Return result"""
    try:
        quo = a / b
    except (TypeError, ZeroDivisionError):
        quo = None
    finally:
        print("Inside result: {}".format(quo))
    return (quo)
