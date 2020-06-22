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

if __name__ == '__main__':
    unittest.main()
