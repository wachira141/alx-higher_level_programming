#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        sqr = []
        for row in matrix:
            newl = []
            for col in row:
                newl.append(col ** 2)
            sqr.append(newl)
        return sqr
