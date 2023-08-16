#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixes = matrix.copy()

    for p in range(len(matrix)):
        matrixes[p] = list(map(lambda x: x**2, matrix[p]))

    return (matrixes)
