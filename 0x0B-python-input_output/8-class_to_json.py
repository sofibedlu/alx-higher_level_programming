#!/usr/bin/python3
"""Define a function 'class_to_json' """


def class_to_json(obj):
    """returns the dictionary discription with simple data structure
        for JSON serialization of an object
    Args:
        obj: instance of a class
    """
    return vars(obj)
