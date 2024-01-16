import sys
import io
import unittest
try:
    from for_loop_operations import *
except ModuleNotFoundError:
    from lesson4.for_loop_operations import *

class TestLoopOperations(unittest.TestCase):
    def setUp(self):
        self.stdout_backup = sys.stdout
        sys.stdout = io.StringIO()

    def tearDown(self):
        sys.stdout = self.stdout_backup

    def test_print_numbers(self):
        print_numbers(5)
        output = sys.stdout.getvalue()
        expected_output = "1\n2\n3\n4\n5\n"
        self.assertEqual(output, expected_output)

    def test_print_numbers_reverse(self):
        print_numbers_reverse(5)
        output = sys.stdout.getvalue()
        expected_output = "5\n4\n3\n2\n1\n"
        self.assertEqual(output, expected_output)

    def test_print_numbers_even(self):
        print_numbers_even(5)
        output = sys.stdout.getvalue()
        expected_output = "2\n4\n"
        self.assertEqual(output, expected_output)

    def test_print_numbers_even_reverse(self):
        print_numbers_even_reverse(5)
        output = sys.stdout.getvalue()
        expected_output = "4\n2\n"
        self.assertEqual(output, expected_output)

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

    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3]), 1)
        self.assertEqual(find_min([3, 2, 1]), 1)
        self.assertEqual(find_min([0, -1, -2]), -2)
        self.assertEqual(find_min([10]), 10)

    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3]), 3)
        self.assertEqual(find_max([3, 2, 1]), 3)
        self.assertEqual(find_max([-2, -1, 0]), 0)
        self.assertEqual(find_max([10]), 10)

    def test_max_min_diff(self):
        self.assertEqual(max_min_diff([1, 2, 3]), 2)
        self.assertEqual(max_min_diff([3, 2, 1]), 2)
        self.assertEqual(max_min_diff([-2, -1, 0]), 2)
        self.assertEqual(max_min_diff([10]), 0)
        self.assertEqual(max_min_diff([10, 10, 10]), 0)

if __name__ == '__main__':
    unittest.main()
