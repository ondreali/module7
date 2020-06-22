"""
program: test_sort_and_search_array.py
Author: Ondrea Li
Last date modfied: 06/21/20
The purpose of this program is to test sort_and_search_array.py
"""

import unittest
from unittest.mock import patch
from fun_with_collections import sort_and_search_array as ssa


class TestList(unittest.TestCase):
    def test_search_array(self):
        self.assertEqual(ssa.search_array('6.9'), 5)
    def test_for_item_found(self):
        self.assertEqual(ssa.search_array(2.3), 1)
    def test_for_item_not_found(self):
        self.assertEqual(ssa.search_array(5.2), None)
        
if __name__ == '__main__':
    unittest.main()
