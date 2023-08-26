def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
my_dict = {'a': 1, 'b': 2, 'c': 3}
update_dictionary(my_dict, 'b', 10)  
update_dictionary(my_dict, 'd', 4)   
print(my_dict)
