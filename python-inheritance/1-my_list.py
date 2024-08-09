#!/usr/bin/python3
"""Class that inherits from the built-in list class."""
class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints the list in a sorted order."""
        print(sorted(self))
