#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    length = len(my_list)
    for elem in range(length):
        if my_list[elem] == search:
            new_list[elem] = replace
    return new_list
