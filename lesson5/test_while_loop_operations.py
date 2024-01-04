import unittest
from lesson5.while_loop_operations import *

class TestWhileLoopOperations(unittest.TestCase):

    def test_find_first_divisible(self):
        self.assertEqual(find_first_divisible(50, 7), 56)
        self.assertEqual(find_first_divisible(100, 13), 104)

    def test_accumulate_squares(self):
        self.assertEqual(accumulate_squares(30), [1, 4, 9, 16, 25])
        self.assertEqual(accumulate_squares(100), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

    def test_count_until_limit(self):
        self.assertEqual(count_until_limit("hello world", "l"), 3)
        self.assertEqual(count_until_limit("hello world", "z"), 0)

    def test_decrement_to_zero(self):
        self.assertEqual(decrement_to_zero(5), [5, 4, 3, 2, 1, 0])
        self.assertEqual(decrement_to_zero(3), [3, 2, 1, 0])

if __name__ == '__main__':
    unittest.main()
