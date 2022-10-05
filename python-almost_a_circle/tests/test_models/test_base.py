#!/usr/bin/python3
""" base test """

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test for base class"""

    def test_isinstance(self):
        """test for is isntance"""
        b1 = Base()
        self.assertIsInstance(b1, Base)

    def test_positive(self):
        """test for number positive"""
        case = Base(25)
        self.assertEqual(case.id, 25)

