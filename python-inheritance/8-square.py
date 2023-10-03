#!/usr/bin/python3
""" Inherits from rectangle """
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """ A class to define a square using rectangle. """
    def __init__(self, size):
        """ initialize an size of rectangle"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns the square of the rectangle """
        return self.__size * self.__size

    def __str__(self):
        """ Returns the print() and str() representation of rectangle """
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__size) + "/" + str(self.__size)
        return string
