#!/usr/bin/python3
"""

A function that determines if an object is an instance of a specified class
"""


def is_same_class(obj, a_class):
    """

    Args:
    obj: The object to check.
    a_class: The class to match the type of obj to.

    """

    return type(obj) == a_class
