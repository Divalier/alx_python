#!/usr/bin/python3
'''
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)
without importing any modules
'''
class Square:
    "building a class that binds a self int"
    def __init__(self, size):
        self.__size = size