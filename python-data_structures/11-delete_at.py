#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return my_list
    large = len(my_list)
    for i in range(large):
        if i == idx:
            del my_list[idx]
            return my_list
        elif idx < 0:
            return my_list
        elif idx >= large:
            return my_list
