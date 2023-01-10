#!/usr/bin/python3
"""Define a function 'load_from_json_file'"""
import json


def load_from_json_file(filename):
    """creates an object from a 'JSON file'
    Args:
        filename: json file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
