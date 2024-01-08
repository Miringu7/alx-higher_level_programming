#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """function that adds 2 tuples."""
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            tuple_a = tuple_a[0], 0
        elif len(tuple_a) == 0:
            tuple_a = 0, 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            tuple_b = tuple_b[0], 0
        elif len(tuple_b) == 0:
            tuple_b = 0, 0
    first_elem = tuple_a[0] + tuple_b[0]
    second_elem = tuple_a[1] + tuple_b[1]
    new_tuple = (first_elem, second_elem)
    return new_tuple
