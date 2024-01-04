import unittest
from lesson7.function_operations import *

class TestFunctionOperations(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(7, 6), 42)
        self.assertEqual(multiply_numbers(-1, 8), -8)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("python"))

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(100), 37.7778, places=4)

if __name__ == '__main__':
    unittest.main()
