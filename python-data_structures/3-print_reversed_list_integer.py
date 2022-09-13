#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    for i in range(int(size / 2)):
        num = my_list[i]
        my_list[i] = my_list[size - i - 1]
        my_list[size - i - 1] = num
    for i in my_list:
        print("{:d}".format(i))
