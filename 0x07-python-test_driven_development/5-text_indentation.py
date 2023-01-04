#!/usr/bin/python3
"""Define function text_indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after
        after each of these charater '.', '?' and ':'
    Args:
        text (str): the input text
    Raises:
        TypeError: if text is not string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    x = 0
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print("{}".format(i))
            print("")
            x = 1
            continue
        if x == 1:
            if i == " " or i == "   ":
                continue
            x = 0
        print("{}".format(i), end="")
