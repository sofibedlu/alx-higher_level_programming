#!/usr/bin/python3
"""Define a function append_write"""


def append_write(filename="", text=""):
    """appends a string at the end of a textfile (UTF8)
    Args:
        filename (text file): text file
        text (str): string
    Returns:
        the number of char added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        nb_char = f.write(text)
    return nb_char
