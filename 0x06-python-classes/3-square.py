#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """represent square object"""
    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of the square
            """
        if not(isinstance(size, int)):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """calculete the area of square
        Returns:
            int: area of a suare
        """
        return (self.__size * self.__size)
