#!/usr/bin/python3
"""Define a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represent Square instances"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the Square instances
        Args:
            size (int): size of the Square instances
            x, y (int): coordinates on the Square instances
            id (int): id number of Square instances
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string for the instances when we call print function"""
        string = '[' + str(self.__class__.__name__) + ']'
        string += ' (' + str(self.id) + ') '
        string += str(self.x) + '/' + str(self.y)
        string += ' - ' + str(self.width)
        return string

    @property
    def size(self):
        """get or set the size of a Square instance"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes of Square instances
        Args:
            args (tuple): -list of arguments not keyworded arg
                          -the order of argument is important:
                                1st argument - id attribute
                                2nd >>       - size >>
                                3rd >>       - x    >>
                                4th >>       - y    >>
            kwargs (dict): -keyworded argument
                           -Each key in the dictionary represents an attribute
                        to the instance and order of argument is not important
        """
        if not bool(args) and bool(kwargs):
            for key in kwargs:
                if key == 'id' and kwargs[key] is not None:
                    self.id = kwargs[key]
                elif key == 'size':
                    self.size = kwargs[key]
                elif key == 'x':
                    self.x = kwargs[key]
                elif key == 'y':
                    self.y = kwargs[key]
        else:
            try:
                if args[0] is not None:
                    self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return

    def to_dictionary(self):
        """returns dictionary representation of Square instances"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
