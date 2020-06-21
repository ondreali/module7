"""
program: test_sort_and_search_list
Author: Ondrea Li
Last date modfied: 06/20/20
The purpose of this program is to test sort_and_search_list
"""

import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_list as ss

class TestList(unittest.TestCase):
    def test_for_item_found(self):
        self.assertEqual(ss.search_list('llama'), 2)
    def test_for_item_not_found(self):
        with self.assertRaises(ValueError):
            ss.search_list('cat')

if __name__ == '__main__':
    unittest.main()
