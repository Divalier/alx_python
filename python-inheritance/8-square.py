#!/usr/bin/env/python3
"""
Write a class Square that inherits from Rectangle (7-rectangle.py):

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented

"""
class BaseGeometry:
    """
    A geometry class.
    """

    def area(self):
       
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    A geometry class.
    """

    def __init__(self, width, height):
        
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
       
        return self.__width * self.__height

    def __str__(self):
        
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    

    def __init__(self, size):
        
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        
        return f"[Square] {self.__width}"
