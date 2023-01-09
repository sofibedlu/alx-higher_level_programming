#!/usr/bin/python3
"""Define a class Mylist"""


class MyList(list):
    """represent a list by inherting list class
    """

    def print_sorted(self):
        """print the list sorted"""
        if not all(isinstance(el, int) for el in self):
            raise TypeError('elements of the list must be integer')
        print(sorted(self))
