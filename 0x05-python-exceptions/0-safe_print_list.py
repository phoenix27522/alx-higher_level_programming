#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    len_l = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            len_l += 1

    except IndexError:
        pass

    print()

    return(len_l)
