#!/usr/bin/env/python3
"""
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

Prototype: def is_kind_of_class(obj, a_class):
You are not allowed to import any module
"""
def is_kind_of_class(obj, a_class):
    "building a class that returns type of object to be class"
    return isinstance(obj, a_class)
