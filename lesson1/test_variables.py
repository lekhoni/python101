
import unittest

from variables import number, name, pi, is_valid, user_info, color_list


class TestVariables(unittest.TestCase):

    def test_number(self):
        """Test for integer variable"""
        self.assertIsInstance(number, int)

    def test_name(self):
        """Test for string variable"""
        self.assertIsInstance(name, str)

    def test_pi(self):
        """Test for float variable"""
        self.assertIsInstance(pi, float)

    def test_is_valid(self):
        """Test for boolean variable"""
        self.assertIsInstance(is_valid, bool)

    def test_user_info(self):
        """Test for dictionary variable"""
        self.assertIsInstance(user_info, dict)

    def test_color_list(self):
        """Test for list variable"""
        self.assertIsInstance(color_list, list)


if __name__ == '__main__':
    unittest.main()