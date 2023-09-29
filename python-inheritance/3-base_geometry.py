#!/usr/bin/env/python3
""" 
       Write an empty class BaseGeometry.

You are not allowed to import any module
"""
class TypeMetaClass(type):
    "building a class that returns type of object to be class"

    def __dir__(cls) -> None:
        
        attributes = super().__dir__()

        return [attribute for attribute in attributes if attribute != '__init_subclass__']
class BaseGeometry(metaclass=TypeMetaClass):
    "building a class that returns the geometry"

    pass

    def __dir__(cls) -> None:
        
        attributes = super().__dir__()

        return [attribute for attribute in attributes if attribute != '__init_subclass__']