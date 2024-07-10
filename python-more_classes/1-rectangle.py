#!/usr/bin/python3
"""Rectangle class that defines a rectangle """


class Rectangle:
    """ __init__ - initialize a rectangle class

    Args:
    width - width initialise at 0
    must be positive and an integer
    heigth -heigth initialise at 0
    must be positive and an integer

    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """ Retrieve the instance attribute of width """
    @property
    def width(self):
        return (self.__width)

    """ Retrieve the instance attribute of height """
    @property
    def height(self):
        return (self.__height)

    """ Set the width """
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """ Set the height """
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
