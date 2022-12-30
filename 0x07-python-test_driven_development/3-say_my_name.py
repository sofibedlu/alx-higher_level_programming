#!/usr/bin/python3
""" Define a function say_my_name"""


def say_my_name(first_name, last_name=""):
    """print full name
    Args:
        first_name: (str)
        last_name: (str)
    Raises:
        TypeError: if either of first_name or last_name is not
                    string
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
