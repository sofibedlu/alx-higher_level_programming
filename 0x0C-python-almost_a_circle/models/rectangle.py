#!/usr/bin/python3
"""Define the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """represent Rectangle instances it inherits from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the Rectangle instance
        Args:
            width: width of the Rectangle instances
            height: height of the Rectangle instances
            x, y: coordinates on the instances
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get or set width of a Recatngle instances"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get or set width of a Rectangle instances"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get or set x-coordinates of the Rectangle instances"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get or set y-coordinates of the Rectangle instances"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of a Rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """print in stdout the Rectangle instance with the character #"""
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """this return a string when we call print of the instance"""
        string = '[' + str(self.__class__.__name__) + ']'
        string += ' (' + str(self.id) + ') ' + str(self.x) + '/' + str(self.y)
        string += ' - ' + str(self.width) + '/' + str(self.height)
        return string

    def update(self, *args, **kwargs):
        """update attributes of the Rectangle instances
        Args:
            args (tuple):
                argument order is important and lebeld as follow:
                1st argument - id attr
                2nd >>       - width attr
                3rd >>       - height attr
                4th >>       - x attr
                5th >>       - y attr
            kwargs (dict): -key-worded argument
                           -Each key in the dictionary represents
                            an attribute to the instance
                           -Argument order is not important
        """
        if not bool(args) and bool(kwargs):
            for key in kwargs:
                if key == 'id' and kwargs[key] is not None:
                    self.id = kwargs[key]
                elif key == 'width':
                    self.width = kwargs[key]
                elif key == 'height':
                    self.height = kwargs[key]
                elif key == 'x':
                    self.x = kwargs[key]
                elif key == 'y':
                    self.y = kwargs[key]
        else:
            try:
                if args[0] is not None:
                    self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                return

    def to_dictionary(self):
        """return dictionary representation of a Rectangle instances"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
