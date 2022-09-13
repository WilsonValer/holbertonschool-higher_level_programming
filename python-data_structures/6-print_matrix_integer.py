#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    large_i = len(matrix)
    for i in range(large_i):
        large_j = len(matrix[i])
        for j in range(large_j):
            if j != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][j]), end='')
        print()
