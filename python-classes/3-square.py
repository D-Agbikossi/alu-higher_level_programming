#!/usr/bin/python3
""" This class defines a square raises errors
and return the current square area """


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

    """ Method that returns the current square area """
    def area(self):
        return (self.__size * self.__size)
