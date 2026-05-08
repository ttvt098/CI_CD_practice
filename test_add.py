# test_calculator. py
# Test scripts usually begin with 'test_', the same as test function name.

# Here we'll just use add function as an example:
# test_calculator.py
import pytest
from calculator import add,subtract,multiply, divide
def test_add( ):
 assert add (1, 2) == 3
 assert add (5, -3) == 2
 assert add(-1, -1) == -2
 assert add (0, 0) == 0

def test_subtract( ):
 assert subtract (5, 2) == 3
 assert subtract (-5, -3) == -2
 assert subtract(-1, -1) == 0
 assert subtract (0, 0) == 0

def test_multiply( ):
 assert multiply (1, 2) == 2
 assert multiply (5, -3) == -15
 assert multiply(-1, -1) == 1
 assert multiply (0, 0) == 0

def test_divide( ):
 assert divide (1, 2) == 0.5
 assert divide (6, 3) == 2
 assert divide(-1, -1) == 1
 assert divide (80, 4) == 20
'''
'assert' statements are used to check that the expected behavior of your 
code is consistent with the actual behavior. When the 'assert' 
expression in the test case evaluates to 'True', the test passes. If the 
result is 'False', the test fails and an 'AssertionError' is raised
'''