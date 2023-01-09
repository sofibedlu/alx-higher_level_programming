#!/usr/bin/python3
"""Define class BaseGeometry"""


class BaseGeometry:
    """represent geometry instance"""
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(name, str):
            raise TypeError("name must be string")
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
