#!/usr/bin/python3
""" Class that inherits the attributes references of class list

    Args:
        list: class list

    """
class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """ Method that prints the sorted list """
        print(sorted(self))
