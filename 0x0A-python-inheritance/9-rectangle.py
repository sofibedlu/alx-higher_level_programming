#!/usr/bin/python3
"""Define a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent Rectangle instances"""
    def __init__(self, width, height):
        """intialize the instance
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area of the triangle
        """
        return self.__width * self.__height

    def __str__(self):
        """return a string when print function prints the instance
        """
        return ('[' + str(self.__class__.__name__) + '] ' +
                str(self.__width) + '/' + str(self.__height))
