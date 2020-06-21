"""
program: basic_list
Author: Ondrea Li
Last date modfied: 06/20/20

The purpose of this program is to write the function that asks for 3 user input in a loop.
"""
import unittest
from unittest.mock import patch
from fun_with_collections import basic_list as topic1


class TestList(unittest.TestCase):
    @patch('fun_with_collections.topic1.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), [5, 5, 5])



if __name__ == '__main__':
