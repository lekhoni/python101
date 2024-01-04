import unittest
from lesson4.for_loop_operations import *

class TestLoopOperations(unittest.TestCase):

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(5), 15)
        self.assertEqual(sum_numbers(10), 55)

    def test_multiply_list(self):
        self.assertEqual(multiply_list([1, 2, 3, 4]), 24)
        self.assertEqual(multiply_list([2, 5]), 10)

    def test_count_occurrences(self):
        self.assertEqual(count_occurrences("hello world", "l"), 3)
        self.assertEqual(count_occurrences("hello world", "z"), 0)

    def test_accumulate_even_numbers(self):
        self.assertEqual(accumulate_even_numbers(10), [2, 4, 6, 8, 10])
        self.assertEqual(accumulate_even_numbers(7), [2, 4, 6])

if __name__ == '__main__':
    unittest.main()
