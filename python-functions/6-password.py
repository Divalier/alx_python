def validate_password(password):
    if len(password) < 8:
        return False
    res= False
    upper = False
    lower = False
    digit = False

    for i in password:
        if i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i.isdigit():
            digit = True
        elif i == ' ':
            return False
    if upper and lower and digit:
        res= True
    return res