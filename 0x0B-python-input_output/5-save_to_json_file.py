#!/usr/bin/python3
"""Define a function 'save_to_json_file'"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to text file, using a JSON representation
    Args:
        my_obj (object)
        filename: text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
