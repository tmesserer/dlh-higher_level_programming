#!/usr/bin/python3
"""
This module is used for the project input/output.
It defines a function that creates a json
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"

try:
    added_items = load_from_json_file(filename)
except FileNotFoundError:
    added_items = []
added_items.extend(sys.argv[1:])
save_to_json_file(added_items, filename)
