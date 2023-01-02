#!/usr/bin/python3
"""Module define class Rectangle"""


class Rectangle:
    """represent rectangle objects"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize new instance

            Args:
                width (int)
                height (int)
        """
        Rectangle.number_of_instances += 1
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

    def area(self):
        """return area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """return perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return printable represetation of the rectangle
           represent rectangle with the character '#'
        """
        if self.__height == 0 or self.__width == 0:
            return ("")
        R = []
        for i in range(self.__height):
            for j in range(self.__width):
                R.append(str(self.print_symbol))
            if i == self.__height - 1:
                continue
            R.append('\n')

        return ("".join(R))

    def __repr__(self):
        """Return printable representation of the rectangle
            return string representation of rectangle to be able to recreate
            a new instance using eval()
        """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """print a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area of the instances
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
