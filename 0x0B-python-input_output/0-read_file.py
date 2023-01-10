#!/usr/bin/python3
"""Define a function to read a file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout
    Args:
        filename (file object): text file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        f1 = f.read()
        print(f1, end="")
