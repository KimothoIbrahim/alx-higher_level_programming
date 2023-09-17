#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    number = len(sys.argv)

    if number - 1 == 1:
        print(f"{number - 1} argument:")
    elif number - 1 > 1:
        print(f"{number - 1} arguments:")
    else:
        print(f"{number - 1} arguments.")

    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
