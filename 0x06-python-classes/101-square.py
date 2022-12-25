#!/usr/bin/python3
"""a Square class that defines a square"""


class Square:
    """represent squares instance"""

    def __init__(self, size=0, position=(0, 0)):
        """ intialize the square object
        Args:
            size (int): size of the square
            position (tuple): coordinates on the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set the size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError('position must be a tuple of 2 positive integer')
        self.__position = value

    def area(self):
        """return the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """print the square with the character '#'"""
        if self.__size == 0:
            return ("")
        else:
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                if i == self.__size - 1:
                    continue
                print()
        return ("")
