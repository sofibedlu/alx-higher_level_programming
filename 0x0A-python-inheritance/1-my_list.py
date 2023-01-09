#!/usr/bin/python3
"""Define a class Mylist"""


class MyList(list):
    """represent a list by inherting list class
    """

    def print_sorted(self):
        """print the list sorted"""
        print(sorted(self))
