import unittest
from lesson3.conditional_checks import is_even, greater_than_ten, string_check, compound_condition

class TestConditionalChecks(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))

    def test_greater_than_ten(self):
        self.assertTrue(greater_than_ten(15))
        self.assertFalse(greater_than_ten(8))

    def test_string_check(self):
        self.assertEqual(string_check("hello"), "Short String")
        self.assertEqual(string_check("this is a longer string"), "Long String")

    def test_compound_condition(self):
        self.assertTrue(compound_condition(7, "Python"))
        self.assertFalse(compound_condition(12, "Java"))

if __name__ == '__main__':
    unittest.main()
