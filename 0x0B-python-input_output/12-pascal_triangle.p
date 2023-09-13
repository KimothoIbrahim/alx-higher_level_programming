#!/usr/bin/python3
"""Pascal's Triangle function."""


def pascal_triangle(n):
    """Pascal's Triangle of size n.
    """
    if n <= 0:
        return []

    triA = [[1]]
    while len(triA) != n:
        tri = triA[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triA.append(temp)
    return triA
