#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    multiplications = list(map(lambda t: t[0]*t[1], my_list))
    scores_multiplications_summation = sum(multiplications)
    weights_summation = sum(list(map(lambda t: t[1], my_list)))
    return scores_multiplications_summation / weights_summation
