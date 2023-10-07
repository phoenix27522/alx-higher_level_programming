#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Create a list to store the added elements
    result = []

    # Determine the length of each tuple
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    # Determine the maximum length between the two tuples
    max_length = max(len_a, len_b)

    for i in range(max_length):
        a_value = tuple_a[i] if i < len_a else 0

        b_value = tuple_b[i] if i < len_b else 0
        # Add the elements together
        add = a_value + b_value
        result.append(add)

    return tuple(result)
