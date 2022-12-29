#!/usr/bin/python3
"""contain function that adds to integer"""


def add_integer(a, b=98):
    """add two integers

    Args:
        a (int): the first number
        b (int): the second number
    Returns:
        sum of the two number
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
