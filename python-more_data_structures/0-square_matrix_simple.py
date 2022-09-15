#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    large = len(matrix)
    new_list = matrix[:]
    for row in range(large):
        large_2 = len(matrix[0])
        new_list[row] = matrix[row][:]
        for elem in range(large_2):
            new_list[elem] = matrix[row][elem] ** 2
    return new_list
