#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_basic(self):
        """ Basic test case for max integer in ordered list """
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_second(self):
        """ Basic second test case for max integer in list """
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
