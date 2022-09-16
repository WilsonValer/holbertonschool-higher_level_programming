#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set(my_list)
    suma = 0
    for num in unique_list:
        suma += num
    return suma
