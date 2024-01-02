import unittest
import os
from file_operations import *

class TestFileOperations(unittest.TestCase):

    def setUp(self):
        # Setup a text file to be used by the tests
        self.test_file = "testfile.txt"
        with open(self.test_file, "w") as f:
            f.write("Hello\nWorld\n")

    def tearDown(self):
        # Clean up the file after tests run
        try:
            os.remove(self.test_file)
        except OSError:
            pass

    def test_read_file(self):
        self.assertEqual(read_file(self.test_file), "Hello\nWorld\n")

    def test_write_file(self):
        write_file(self.test_file, "New content")
        self.assertEqual(read_file(self.test_file), "New content")

    def test_append_to_file(self):
        append_to_file(self.test_file, "\nMore content")
        self.assertEqual(read_file(self.test_file), "Hello\nWorld\n\nMore content")

    def test_file_exists(self):
        self.assertTrue(file_exists(self.test_file))
        self.assertFalse(file_exists("nonexistentfile.txt"))


if __name__ == '__main__':
    unittest.main()
