#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square object"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize the square
            Args:
                size (int): size of the square
                position (int, int): coordinates on the square
            """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set size to the square"""
        if not(isinstance(value, int)):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """to retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """to set position"""
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(n, int) for n in value)
                or not all(n >= 0 for n in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """return current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for k in range(self.size):
                    print("#", end="")
                print()
