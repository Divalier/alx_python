#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
num= str(number)
lnum= int(num[-1:])
if lnum >5:
    print(f"Last digit of {number} is {lnum} and is greater than 5")
if lnum ==0:
    print(f"Last digit of {number} is {lnum} and is 0")
if lnum<6 and  not lnum == 0:
    print(f"Last digit of {number} is {lnum} aand is less than 6 and not 0")