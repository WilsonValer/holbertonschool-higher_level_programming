#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for i in my_list:
        if i == idx:
            other_list = my_list[:]
            my_list[idx] = element
            return other_list
        elif idx < 0:
            return my_list
        elif idx > len(my_list):
            return my_list