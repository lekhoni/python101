import unittest
from string_operations import *

class TestStringOperations(unittest.TestCase):

    def test_concatenate(self):
        self.assertEqual(concatenate("Hello", "World"), "HelloWorld")
        self.assertEqual(concatenate("Foo", "Bar"), "FooBar")

    def test_find_substring(self):
        self.assertEqual(find_substring("Hello World", "World"), True)
        self.assertEqual(find_substring("Hello World", "world"), False)

    def test_to_upper(self):
        self.assertEqual(to_upper("hello"), "HELLO")
        self.assertEqual(to_upper("Hello World"), "HELLO WORLD")

    def test_to_lower(self):
        self.assertEqual(to_lower("HELLO"), "hello")
        self.assertEqual(to_lower("Hello World"), "hello world")

    def test_replace_substring(self):
        self.assertEqual(replace_substring("Hello World", "World", "Python"), "Hello Python")
        self.assertEqual(replace_substring("Foo Bar Baz", "Bar", "Foo"), "Foo Foo Baz")

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_string_length(self):
        self.assertEqual(string_length("hello"), 5)
        self.assertEqual(string_length(""), 0)

    # Additional tests for slicing, counting characters, etc.
    # ... add more tests up to 20 or more for various operations ...

if __name__ == '__main__':
    unittest.main()
