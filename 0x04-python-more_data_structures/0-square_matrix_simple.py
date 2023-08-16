#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = matrix.copy()

    for t in range(len(matrix)):
        mat[t] = list(map(lambda x: x**2, matrix[t]))

    return (mat)
