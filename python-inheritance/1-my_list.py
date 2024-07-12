#!/usr/bin/python3
"""Defines an inherited class MyList"""


class MyList(list):
    """
    A subclass of list that includes a method to print the list in ascending order
    """

    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        if issubclass(MyList, list):
            print(sorted(self))
