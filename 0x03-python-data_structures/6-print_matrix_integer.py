#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # r = rows and c = columns
    for r in matrix:
        for c in r:
            if c != r[-1]:
                print("{:d}".format(c), end=" ")

            else:
                print("{:d}".format(c))
