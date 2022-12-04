#!/usr/bin/pythton3
def print_matrix_integer(matrix=[[]]):
    size = len(matrix[0])
    for i in matrix:
        col = 0
        for j in i:
            if col == size - 1:
                print("{:d}".format(j), end="")
            else:
                print("{:d} ".format(j), end="")
            col += 1
        print()
