#!/usr/bin/python3
def max_integer(my_list=[]):
    large = len(my_list)
    if not my_list:
        return None
    biggest = [0]
    for i in range(0, large):
        if my_list[i] > biggest[0]:
            biggest[0] = my_list[i]
    return biggest[0]
