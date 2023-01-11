#!/usr/bin/python3
"""Define a Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents Square instances"""
    def __init__(self, size):
        """intialize the instance
        Args:
            size (int): size of a square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
