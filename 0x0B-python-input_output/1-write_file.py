#!/usr/bin/python3
"""Define a function that writes to file"""


def write_file(filename="", text=""):
    """writes a string to a text file(utf-8)
    Args:
        filename (file object): text file
        text (str): string
    Returns:
        the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        nb_char = f.write(text)
    return nb_char
