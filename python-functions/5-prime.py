def is_prime(number):
    if  number ==2:
        return True
    if number <= 1 or number % 2 == 0 or number %3 ==0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True





