#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    # Initialize the maximum value as the first element of the list
    maxi = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > maxi:
            maxi = my_list[i]

    return maxi
