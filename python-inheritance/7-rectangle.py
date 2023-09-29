#!/usr/bin/env/python3
"""
Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py). (task based on 6-rectangle.py)

Instantiation with width and height: def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>
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
    

    def __init__(self, width, height):
        
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        
        return self.__width * self.__height

    def __str__(self):
        
        return f"[Rectangle] {self.__width}/{self.__height}"
