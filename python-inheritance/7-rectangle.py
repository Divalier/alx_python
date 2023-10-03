#!/usr/bin/python3
""" Inherits from BaseGeometry """
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class to define a rectangle using base geometry. """
    def __init__(self, width, height):
        """ initialize a new rectangle """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height
    def __str__(self):
        """ Returns the print() and str() representation of rectangle """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
