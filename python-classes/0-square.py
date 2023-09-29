#!/usr/bin/python3
'''
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
'''
class Square:
    "class Square is the blueprint to create a class and an object"
    " Additionally self, isa keyword that binds the actual value with object"
    "The self is used to initialize an object and is always called out everytme a new object is created"
    def __init__(self, size):
        self.__size = size