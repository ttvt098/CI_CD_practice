# test_calculator_unittest.py
import unittest
import random
from calculator import add, subtract, multiply, divide
NUM_TESTS = 20
#In this case, since we have '_main_' in the code, so just simply run this test will be OK:
class TestCalculator(unittest.TestCase) :
 def test_add (self) :
    for _ in range (NUM_TESTS) :
        x = random. uniform(-1000, 1000)
        y = random. uniform(-1000, 1000)
        self.assertAlmostEqual (add (x, y) , x + y)

 def test_subtract (self) :
    for _ in range (NUM_TESTS) :
        x = random. uniform(-1000, 1000)
        y = random. uniform(-1000, 1000)
        self.assertAlmostEqual (subtract (x, y) , x - y)

 def test_multiply (self) :
    for _ in range (NUM_TESTS) :
        x = random. uniform(-1000, 1000)
        y = random. uniform(-1000, 1000)
        self.assertAlmostEqual (multiply (x, y) , x * y)

 def test_divide (self) :
    for _ in range (NUM_TESTS) :
        x = random. uniform(-1000, 1000)
        y = random. uniform(-1000, 1000)
        self.assertAlmostEqual (divide (x, y) , x / y)
if __name__ == '__main__':
 unittest.main ()