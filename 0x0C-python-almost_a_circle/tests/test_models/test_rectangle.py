#!/usr/bin/python3
import unittest

from models.rectangle import Rectangle
from models.base import Base

class TestBase(unittest.TestCase):
    def test_rectangle(self):
        """test cases"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
    	r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
    	self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
    	r3.id = "a"
        self.assertEqual(r3.id, "a")
