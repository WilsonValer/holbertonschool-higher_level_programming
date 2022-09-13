#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    large_a = len(tuple_a)
    large_b = len(tuple_b)
    if large_a == 2 and large_b == 2:
        return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    else:
        tuple_a = tuple_a + (0, 0)
        tuple_b = tuple_b + (0, 0)
        return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
