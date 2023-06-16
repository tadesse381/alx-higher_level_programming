#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_mtrx = []

    if len(matrix) > 0:
        for elems in matrix[:]:
            n_mtrx.append(list(map(lambda x: x ** 2, elems)))

    return n_mtrx
