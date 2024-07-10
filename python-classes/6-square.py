#!/usr/bin/python3
""" This class defines a square, raises errors,
acces and update attribute and return the current square area """


class Square:
    """ __init__ - initialize a square class

    Args:
    size - size initialise at 0
    must be positive and an integer
    position - initialise at 0
    must be a tuple of 2 positive integer

    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self. position = position

    """ Retrieve the instance attribute  size """
    @property
    def size(self):
        return (self.__size)

    """ Retrieve the instance attribute  position """
    @property
    def position(self):
        return (self.__position)

    """ Set the size """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ Set the position """
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """ Method that returns the current square area """
    def area(self):
        return (self.__size ** 2)

    """ This method prints in stdout the square with the character #
    and use space for position"""
    def my_print(self):
        if(self.size == 0):
            print()
            return

        for x in range(self.position[1]):
            print()
        for x in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
