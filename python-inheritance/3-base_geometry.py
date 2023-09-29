#!/usr/bin/env/python3
""" 
       Write an empty class BaseGeometry.

You are not allowed to import any module
"""
class TypeMetaClass(type):
   
    def __dir__(cls) -> None:
        
        attributes = super().__dir__()

        return [attribute for attribute in attributes if attribute != '__init_subclass__']
class BaseGeometry(metaclass=TypeMetaClass):
    
    pass

    def __dir__(cls) -> None:
        
        attributes = super().__dir__()

        return [attribute for attribute in attributes if attribute != '__init_subclass__']