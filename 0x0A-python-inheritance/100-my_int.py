#!/usr/bin/python3
"""Define a class MyInt"""


class MyInt(int):
    """it inherits int class and has == and !=
        operators inverted
    """
    def __eq__(self, other):
        return self.real != other

    def __ne__(self, other):
        return self.real == other
