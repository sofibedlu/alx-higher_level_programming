#!/usr/bin/python3
"""Module define class Rectangle"""


class Rectangle:
    """represent rectangle objects"""
    def __init__(self, width=0, height=0):
        """initialize new instance

            Args:
                width (int)
                height (int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """to retrieve or set width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """to retrieve or set height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
