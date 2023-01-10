#!/usr/bin/python3
"""Define a function 'from_json_string'"""
import json


def from_json_string(my_str):
    """returns an object (python data structure) represented by a JSON string
    """
    return json.loads(my_str)
