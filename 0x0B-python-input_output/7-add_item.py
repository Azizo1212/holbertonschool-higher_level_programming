#!/usr/bin/python3
"""adds all arguments to a Python list"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", "a")
try:
    new_list = load_from_json_file("add_item.json")
except ValueError:
    new_list = []
save_to_json_file(new_list + sys.argv[1:], "add_item.json")
