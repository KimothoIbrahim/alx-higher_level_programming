#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixes = matrix.copy()

    for x in range(len(matrix)):
        matrixes[x] = list(map(lambda x: x**2, matrix[x]))

    return (matrixes)
