#!/usr/bin/python3
""" Define a class Square"""


class Square:
    """ represent a square"""

    def __init__(self, size=0):
        """initialize the square
        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """return the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size of the square
        Args:
            value (int): size of the square
        """
        if not(isinstance(value, int)):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """return area of a square"""
        return (self.__size * self.__size)
