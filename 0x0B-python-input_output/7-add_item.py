#!/usr/bin/python3
"""adds all arguments to a python list, and save them to a file
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    obj = []
for i in range(1, len(argv)):
    obj.append(argv[i])
save_to_json_file(obj, "add_item.json")
