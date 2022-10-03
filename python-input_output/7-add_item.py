#!/usr/bin/python3
import sys
import os.path
"""This program take the file add_item.json, and add the
parameters to the list inside this file.
- If the file doesn't exist create it.
- If no exist parameters do nothing or
create the list if the file is empty.
"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


my_list = []
if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")
