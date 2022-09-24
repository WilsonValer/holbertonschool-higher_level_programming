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
        result = max_integer([-5, -7, -1], -1)
        self.assertEqual(result, -1)

    def string():
        with self.assertRaises(TypeError):
            max_integer([-5, "wilson"])

    def error():
        result = max_integer([7, 6, "string"])
        self.assertIsInstance(result, int, "validate type")




if __name__ == '__main__':
    unittest.main()
