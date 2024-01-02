
import unittest


class TestVariables(unittest.TestCase):

    def test_number(self):
        """Test for integer variable"""
        from variables import number
        self.assertIsInstance(number, int)

    def test_name(self):
        from variables import name
        """Test for string variable"""
        self.assertIsInstance(name, str)

    def test_pi(self):
        """Test for float variable"""
        from variables import pi
        self.assertIsInstance(pi, float)

    def test_is_valid(self):
        """Test for boolean variable"""
        from variables import is_valid
        self.assertIsInstance(is_valid, bool)

    def test_user_info(self):
        """Test for dictionary variable"""
        from variables import user_info
        self.assertIsInstance(user_info, dict)

    def test_color_list(self):
        """Test for list variable"""
        from variables import color_list
        self.assertIsInstance(color_list, list)


if __name__ == '__main__':
    unittest.main()