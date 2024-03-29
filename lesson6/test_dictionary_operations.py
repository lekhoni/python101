import unittest

class TestDictionaryOperations(unittest.TestCase):

    def test_add_entry(self):
        from dictionary_operations import add_entry
        dictionary = {'apple': 1, 'banana': 2}
        result = add_entry(dictionary, 'cherry', 3)
        self.assertEqual(result, {'apple': 1, 'banana': 2, 'cherry': 3})

    def test_remove_entry(self):
        from dictionary_operations import remove_entry
        dictionary = {'apple': 1, 'banana': 2, 'cherry': 3}
        result = remove_entry(dictionary, 'banana')
        self.assertEqual(result, {'apple': 1, 'cherry': 3})

    def test_update_entry(self):
        from dictionary_operations import update_entry
        dictionary = {'apple': 1, 'banana': 2}
        result = update_entry(dictionary, 'apple', 5)
        self.assertEqual(result, {'apple': 5, 'banana': 2})

    def test_get_entry(self):
        from dictionary_operations import get_entry
        dictionary = {'apple': 1, 'banana': 2}
        result = get_entry(dictionary, 'banana')
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
