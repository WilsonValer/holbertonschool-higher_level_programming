#!/usr/bin/python3
"""
    script that adds all arguments to a Python list,
    and then save them to a file:
    You must use your function save_to_json_file from
    7-save_to_json_file.py
    You must use your function load_from_json_file
    from 8-load_from_json_file.py
    The list must be saved as a JSON representation
    in a file named add_item.json
    If the file doesn’t exist, it should be created
    You don’t need to manage file permissions / exceptions.
"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

lenght = len(sys.argv)
my_list = []
address = "add_item.json"

for i in range(1, lenght):
    my_list.append(sys.argv[i])

new_list = load_from_json_file(address)

for elem in my_list:
    new_list.append(elem)

save_to_json_file(new_list, address)
