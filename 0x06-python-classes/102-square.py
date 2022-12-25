#!/usr/bin/python3
"""define a Class called Square used to create square instance"""


class Square:
    """represent a square instance"""

    def __init__(self, size=0):
        """intialize the square
        Args:
            size (int): size of the current instance
        """
        self.size = size

    @property
    def size(self):
        """return size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """get the area"""
        return self.__size * self.__size

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
