#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """represent a square object"""

    def __init__(self, size=0):
        """initialize the square
        Args:
            size (int): size of the square
            """
        self.__size = size

    @property
    def size(self):
        """to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set the size for the square
        Args:
            value (int): size
        """
        if not(isinstance(value, int)):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """return the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character '#'"""
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
