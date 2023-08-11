#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    for numba in range(1, 101):
        if numba % 3 == 0 and numba % 5 == 0:
            print("FizzBuzz ", end="")
        elif numba % 3 == 0:
            print("Fizz ", end="")
        elif numba % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numba), end="")
