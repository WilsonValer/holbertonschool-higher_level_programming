#!/usr/bin/python3
"""This program take the file add_item.json, and add the
parameters to the list inside this file.
- If the file doesn't exist create it.
- If no exist parameters do nothing or create the list if the file is empty.
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
