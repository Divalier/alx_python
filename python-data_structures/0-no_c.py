def no_c(my_string):
    contain = []
    for char in my_string:
        if char != 'c' and char != 'C':
            contain.append(char)
    result = ''.join(contain)
    return result
