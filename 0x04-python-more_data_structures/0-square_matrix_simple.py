#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    a = new_matrix[0]
    b = new_matrix[1]
    c = new_matrix[2]
    a = list(map(lambda x: x*x, a))
    b = list(map(lambda x: x*x, b))
    c = list(map(lambda x: x*x, c))
    new_matrix = [a, b, c]
    return new_matrix
