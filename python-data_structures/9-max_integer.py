#!/usr/bin/python3


def max_integer(my_list=[]):
    if not my_list:
        return None

    max = my_list[0]
    for x in my_list[1:]:
        if x > max:
            max = x

    return (max)
