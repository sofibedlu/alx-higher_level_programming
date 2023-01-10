#!/usr/bin/python3
"""Define a function to_json_string"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object(string)
    """
    return json.dumps(my_obj)
