#!/usr/bin/python3
"""Define is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """return True if the object is instance of, or if the object is
        an instance of a class that inherited from
    Args:
        obj: object
        a_class: class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
