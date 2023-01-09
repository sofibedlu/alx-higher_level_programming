#!/usr/bin/python3
"""Define a function inherites_from"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
        that inherited(directly or indirectly) from the specified class
        otherwise False
    Args:
        obj: object(instance)
        a_class: class
    """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    else:
        return False
