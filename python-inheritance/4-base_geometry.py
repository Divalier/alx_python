#!/usr/bin/env/python3
"""
Write a class BaseGeometry (based on 3-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
You are not allowed to import any module
"""


class TypeMetaClass(type):
    "building a class that returns type of object to be class"
    def __dir__(cls) -> None:
        
        attributes = super().__dir__()

        return [attribute for attribute in attributes if attribute != '__init_subclass__']

class BaseGeometry(metaclass=TypeMetaClass):
    "building a class that returns type of object to be class"
    def area(self):
        
        raise Exception("area() is not implemented")
