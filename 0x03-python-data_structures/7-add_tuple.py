#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tmp_tuple_a = tuple_a[:]
    tmp_tuple_b = tuple_b[:]
    if len(tuple_a) == 0:
        tmp_tuple_a = (0, 0)
    if len(tuple_b) == 0:
        tmp_tuple_b = (0, 0)
    if len(tuple_a) == 1:
        tmp_tuple_a = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        tmp_tuple_b = (tuple_b[0], 0)

    return (tmp_tuple_a[0]+tmp_tuple_b[0], tmp_tuple_a[1]+tmp_tuple_b[1])
