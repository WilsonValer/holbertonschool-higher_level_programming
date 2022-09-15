#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    length = len(my_list)
    for elem in range(length):
        if my_list[elem] == search:
            my_list[elem] = 89
    return new_list
