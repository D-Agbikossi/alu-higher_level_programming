#!/usr/bin/python3
""" This class defines a square and raise errors """


class Square:
    """ __init__ - initialize a square class

    Args:
    size - size initialise at 0
    must be positive and an integer

    """
    def __init__(self, size=0):
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
