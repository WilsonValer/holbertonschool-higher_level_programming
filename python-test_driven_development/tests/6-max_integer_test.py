#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Set of test to validate the functionality of the function max integer"""

    def test_doc(self):
        """Validating the documentation in the file"""
        self.assertTrue(len(max_integer.__doc__) > 0)

    def test_max(self):
        """Test normal cases without error"""
        result = max_integer([2, 7, 6])
        assertEqual(result, 6)




if __name__ == '__main__':
    unittest.main()
