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

    """ Introduce public class attribute number_of_instances, print_symbol """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    """ Return the rectangle area """
    def area(self):
        return (self.__width * self.__height)

    """ Return the rectangle perimeter """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2

        return perimeter

    """ Print the rectangle with the character # """
    def __str__(self):
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return (rectangle)
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rectangle += str(self.print_symbol)
                if i < self.__height - 1:
                    rectangle += "\n"
        return(rectangle)

    """ Return a string representation of the rectangle to be able
    to recreate a new instance by using eval() """
    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    """ Print a message when an instance of Rectangle is deleted """
    def __del__(self):

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """ Return the biggest rectangle based on the area """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    """ Return a new Rectangle instance with width == height == size """
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
