#!/usr/bin/env/python3
"""
Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).

Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator

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
