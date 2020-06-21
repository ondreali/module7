"""
program: test_basic_list_exception
Author: Ondrea Li
Last date modfied: 06/20/20

The purpose of this program is to test basic_list_exception.py
"""
import unittest
from unittest.mock import patch
from fun_with_collections import basic_list as topic1

class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), [5, 5, 5])

@patch('fun_with_collections.topic1.get_input', return_value='ab')  # patch function for input
def test_make_list_non_numeric(self, input):                        # pass input
    with self.assertRaises(ValueError):                             # this is familiar
        topic1.make_list()                                          # call the function!

if __name__ == '__main__':
    unittest.main()
