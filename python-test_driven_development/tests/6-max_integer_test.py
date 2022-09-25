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
        self.assertEqual(result, 7)

    def negative(self):
        result = max_integer([-5, -7, -1])
        self.assertEqual(result, -1)

    def string():
        with self.assertRaises(TypeError):
            max_integer([-5, "wilson"])

    def nega_positive():
        result = max_integer([4, 5, -7, 3])
        self.assertEqual(result, 5)
    
    def empty():
        with self.assertRaises(TypeError):
            max_integer([])

    def tes_error():
        result = max_integer([8, 2, "rt"])
        self.assertEqual(result,10, "no is result" )
        self.assertIsInstance(result, int, " validate type")

    def test_None(self):
        self.assertIsNone(max_integer([7, 9, 15]), None,)
        self.assertIsNone(max_integer(), None)
        self.assertIsNone(max_integer([None]), None)


if __name__ == '__main__':
    unittest.main()
