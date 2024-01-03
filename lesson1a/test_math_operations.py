import unittest
import math
from math_operations import *

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 15), 25)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(100, 200), -100)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-7, -8), 56)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

    def test_square(self):
        self.assertEqual(square(4), 16)
        self.assertEqual(square(-3), 9)

    def test_cube(self):
        self.assertEqual(cube(3), 27)
        self.assertEqual(cube(-2), -8)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(54, 7), 5)

    def test_sqrt(self):
        self.assertEqual(sqrt(36), 6)
        self.assertAlmostEqual(sqrt(2), math.sqrt(2))

    # Tests for trigonometric functions
    def test_sin(self):
        self.assertAlmostEqual(sin(math.pi/2), 1)
        self.assertAlmostEqual(sin(math.pi), 0)

    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(math.pi), -1)

    # Tests for logarithmic functions
    def test_log(self):
        self.assertAlmostEqual(log(1), 0)
        self.assertAlmostEqual(log(math.e), 1)

if __name__ == '__main__':
    unittest.main()
