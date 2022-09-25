#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Set of test to validate the functionality of the function max integer"""


    def test_max(self):
        """Test normal cases without error"""
        result = max_integer([2, 7, 6])
        self.assertEqual(result, 7, "wilson ")

    def test_negat_string(self):
        """Test normal cases without error"""
        with self.assertRaises(TypeError):
            result = max_integer([-5, "wilson", -1])

    def test_string(self):
        """Test normal cases without error"""
        with self.assertRaises(TypeError):
            max_integer([-5, "tp"])


    def test_None(self):
        """Test normal cases without error"""
        self.assertIsNone(max_integer([]), None,)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)

    def teste_negatives(self):
        """Test normal cases without error"""
        result = max_integer([-7, -6, -1])
        self.assertEqual(result, -1)

    def test_nega_posi(self):
        """Test normal cases without error"""
        result = max_integer([8, -2, 4, -7])
        self.assertEqual(result, 8)
