#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    def testSizeValidation(self):
        with self.assertRaises(TypeError):
            s1 = Square(True)

        with self.assertRaises(ValueError):
            s1 = Square(-5)

        with self.assertRaises(ValueError):
            s1 = Square(0)

    def testCreateSquare(self):
        s1 = Square(5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(5, 3, 2)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 2)

        s3 = Square(5, id=7)
        self.assertEqual(s3.id, 7)

        s4 = Square(5, x=3, y=9)
        self.assertEqual(s4.x, 3)
        self.assertEqual(s4.y, 9)

    def testUpdateArgs(self):
        s1 = Square(5)
        s1.update(1, 4, 3, 5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 5)

    def testUpdateKwargs(self):
        s1 = Square(5)
        s1.update(size=12, id=3, x=4, y=1)
        self.assertEqual(s1.id, 3)
        self.assertEqual(s1.size, 12)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 1)

    def testStr(self):
        s1 = Square(1, 4, 3, 5)
        expected = "[Square] (5) 4/3 - 1"
        self.assertEqual(str(s1), expected)

        s1.update(size=12, id=3, x=4, y=1)
        expected = "[Square] (3) 4/1 - 12"
        self.assertEqual(str(s1), expected)

    def testToDictionary(self):
        s1 = Square(1, 4, 3, 5)
        s1_dict = s1.to_dictionary()
        expected = {"id": 5, "size": 1, "x": 4, "y": 3}
        self.assertEqual(s1_dict, expected)
