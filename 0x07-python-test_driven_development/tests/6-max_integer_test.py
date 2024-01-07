#!/usr/bin/python3
"""Test max_integer function"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_array(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)

    def test_errors(self):
        self.assertRaises(TypeError, max_integer, 19)
