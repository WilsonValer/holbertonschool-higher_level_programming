#!/usr/bin/python3
"""module test for rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_CodeFormat(unittest.TestCase):
    """ test for rectagle class """
    
    def test_normal(self):
        """test for with diffrente number"""
        r1 = Rectangle(15, 16)
        r1.id = 1
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(15, 16, 7, 10)
        r2.id = 2
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(7, 25, 43)
        r3.id = 3
        self.assertEqual(r3.id, 3)
    
    def test_number_argument(self):
        """test for worg argument"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(7, 9, 5, 1, 3, 15)
        with self.assertRaises(TypeError):
            r1 = Rectangle(12)

class Test_Rectangle_Attributes(unittest.TestCase):
    """method test for task 03"""
    def test_width_height_greaster(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(5, 9)
            r1.width = -6

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2 = Rectangle(16, 18)
            r2.height = -15
    def test_width_height_mustbeinteger(self):
        """width and height must be integer"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle("25", 18)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2 = Rectangle(16, "18")

class Test_Rectangle_are(unittest.TestCase):
    """ test for rea Rectangle task04 """
    def test_area_normal(self):
        """test for area"""
        r1 = Rectangle(3, 5)
        self.assertEqual(r1.area(), 15)

        r2 = Rectangle(15, 2)
        self.assertEqual(r2.area(), 30)

    def test_ares_string(self):
        """ ares string """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-15, 2)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2 = Rectangle("25", 18)
