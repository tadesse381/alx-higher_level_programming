#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for j in matrix:
            n = 1
            length = len(j)

            for k in j:
                if n == length:
                    print('{:d}'.format(k), end='')
                else:
                    print('{:d}'.format(k), end=' ')
                n += 1

            print()
