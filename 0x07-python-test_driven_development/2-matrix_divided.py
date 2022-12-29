#!/usr/bin/python3
"""define a function called matrix_divided"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
        matrix (list): matrix(list of lists)
        div (int, float): the number that divides each element of the lists
    Returns:
        return the new matrix after division
    """
    new_matrix = []
    new_list = []
    i = 0
    if (not isinstance(matrix, list) or
            not all(isinstance(l, list) for l in matrix)
            or not all(isinstance(e, (int, float))
                       for l in matrix for e in l)):
        raise TypeError('matrix must be a matrix (list of lists)'
                        ' of integers/floats')
    if not all(len(matrix[0]) == len(matrix[i]) for i in range(len(matrix))):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for l in matrix:
        for e in l:
            element = e / div
            new_list.append(round(element, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
