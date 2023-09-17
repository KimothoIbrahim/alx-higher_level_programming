#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sumo = 0

    for i in range(1, len(sys.argv)):
        sumo += int(sys.argv[i])

    print(sumo)
