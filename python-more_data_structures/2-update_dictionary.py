#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    my_dict = a_dictionary
    if key in my_dict:
        my_dict[key] = value
    else:
        my_dict[key] = value
    return my_dict
