import unittest
# add function
def add(x, y) :
 return x + y

# Substract fucntion
def subtract(x, y):
 return x - y

# multiply function
def multiply(x, y) :
 return x * y

# divide function
def divide(x, y) :
 # divisor limitation
 if y == 0:
    raise ValueError ("divisor cannot be 0")
 return x/y
