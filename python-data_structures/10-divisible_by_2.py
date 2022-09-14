#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    large = len(my_list)
    if not my_list:
        return
    new_list = []
    for i in range(large):
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
