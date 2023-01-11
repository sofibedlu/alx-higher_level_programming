#!/usr/bin/python3
"""Define a function pascal_traingle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
        the Pascal’s triangle of n
    """
    pascal = [[1]]
    row = []
    r_prev = []

    if n <= 0:
        return []

    for i in range(n):
        if len(r_prev) >= 2:
            for j in range(len(r_prev) - 1):
                ele = r_prev[j] + r_prev[j + 1]
                row.append(ele)
            row.insert(0, 1)
            row.append(1)
            pascal.append(row)
            r_prev = row
            row = []
        else:
            r_prev.append(1)
            if i == 1:
                pascal.append(r_prev)
    return (pascal)
