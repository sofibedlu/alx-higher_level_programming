#!/usr/bin/python3
"""define a function called matrix_divided"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix by div

    Args:
        matrix (list): matrix(list of lists)
        div (int, float): the number that divides each element of the lists
    Returns:
        return the new matrix after division
    Raises:
        TypeError: if matrix is not list of lists of integers or floats
        TypeError: if each row of the matrix is not the same size
        TypeError: if div is not a number(integer or float)
        ZeroDivisionError: if div == 0
    """
    new_matrix = []
    new_list = []
    i = 0
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)
            or not all(isinstance(el, (int, float))
                       for row in matrix for el in row)):
        raise TypeError('matrix must be a matrix (list of lists)'
                        ' of integers/floats')
    if not all(len(matrix[0]) == len(matrix[i]) for i in range(len(matrix))):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for row in matrix:
        for el in row:
            element = el / div
            new_list.append(round(element, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
