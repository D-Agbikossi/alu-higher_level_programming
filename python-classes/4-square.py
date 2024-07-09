#!/usr/bin/python3
""" This class defines a square, raises errors,
acces and update attribute and return the current square area """


class Square:
    """ __init__ - initialize a square class

    Args:
    size - size initialise at 0
    must be positive and an integer

    """
    def __init__(self, size=0):
        self.size = size

    """ Retrieve the instance attribute """
    @property
    def size(self):
        return (self.__size)

    """ Set the size """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ Method that returns the current square area """
    def area(self):
        return (self.__size ** 2)
