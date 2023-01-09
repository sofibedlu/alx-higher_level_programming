#!/usr/bin/python3
"""Define a function is_same_class"""


def is_same_class(obj, a_class):
    """returns True if the object is exaclty an instance of the
        specified class otherwise False
    Args:
        obj: instances
        a_class: class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
