#!/usr/bin/python3
"""Define Square Class"""


class Square:
    """Square represent a square object"""
    def __init__(self, size=0):
        """ instantiate square
        Args:
            size (int): size of the square
            """
        if not(isinstance(size, int)):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
