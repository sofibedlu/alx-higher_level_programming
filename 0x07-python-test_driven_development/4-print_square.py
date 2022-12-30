#!/usr/bin/python3
"""Define a function print_square()"""


def print_square(size):
    """print a square with the character '#'
    Args:
        size (int): size of the square
    Raises:
        TypeError: if size not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
