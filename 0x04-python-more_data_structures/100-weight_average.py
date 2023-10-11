#!/usr/bin/python3
def weight_average(my_list=[]):
    score = list(map(lambda x: x[0] * x[1], my_list))
    div = sum(map(lambda x: x[1], my_list))

    if div == 0:
        return 0
    else:
        return (sum(score) / div)
