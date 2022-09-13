#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if i == idx:
            return my_list[idx]
        elif idx < 0:
            return None
        elif idx > len(my_list):
            return None
