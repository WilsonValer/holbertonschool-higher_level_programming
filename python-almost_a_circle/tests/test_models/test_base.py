#!/usr/bin/python3
""" base test """

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test for base class"""

    def test_isinstance(self):
        """test id for is isntance"""
        b1 = Base()
        self.assertIsInstance(b1, Base)
        b2 = Base(65)
        self.assertIsInstance(b2, Base)

    def test_positive(self):
        """test id for number positive"""
        case = Base(25)
        case_01 = Base()
        case_02 = Base()
        case_03 = Base()
        self.assertEqual(case.id, 25)
        self.assertEqual(case_01.id, 2)
        self.assertEqual(case_02.id, 3)
        self.assertEqual(case_03.id, 4)

    def test_negative(self):
        """test id for negative values"""
        negative_01 = Base(-12)
        negative_02 = Base(-25)
        self.assertEqual(negative_01.id, -12)
        self.assertEqual(negative_02.id, -25)

    def test_string(self):
        """test  id for string case"""
        string_01 = Base("unicornio")
        string_02 = Base("sagitario")
        self.assertEqual(string_01.id, "unicornio")
        self.assertEqual(string_02.id, "sagitario")


