import unittest
from lesson2.list_operations import add_element, remove_element, get_element, modify_element

class TestListOperations(unittest.TestCase):
    def setUp(self):
        self.test_list = [10, 20, 30, 40, 50]

    def test_add_element(self):
        result = add_element(self.test_list, 60)
        self.assertEqual(result, [10, 20, 30, 40, 50, 60])

    def test_remove_element(self):
        result = remove_element(self.test_list, 20)
        self.assertEqual(result, [10, 30, 40, 50])

    def test_get_element(self):
        result = get_element(self.test_list, 2)
        self.assertEqual(result, 30)

    def test_modify_element(self):
        result = modify_element(self.test_list, 1, 25)
        self.assertEqual(result, [10, 25, 30, 40, 50])

if __name__ == '__main__':
    unittest.main()
