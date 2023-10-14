#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def testWidthValidation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10)
        with self.assertRaises(TypeError):
            r = Rectangle("5", 10)

        r = Rectangle(5, 10)
        r.width = 20
        self.assertEqual(r.width, 20)

        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.width = 3.4
        with self.assertRaises(TypeError):
            r.width = True

    def testHeightValidation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, -10)
        with self.assertRaises(TypeError):
            r = Rectangle(5, "10")

        r = Rectangle(5, 10)
        r.height = 20
        self.assertEqual(r.height, 20)

        with self.assertRaises(ValueError):
            r.height = -10
        with self.assertRaises(TypeError):
            r.height = 3.4
        with self.assertRaises(TypeError):
            r.height = True

    def testXValidation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -1)
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, "1")

        r = Rectangle(5, 10, 2)
        r.x = 4
        self.assertEqual(r.x, 4)

        with self.assertRaises(ValueError):
            r.x = -10
        with self.assertRaises(TypeError):
            r.x = 3.4
        with self.assertRaises(TypeError):
            r.x = True

    def testYValidation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 1, -1)
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, 1, "1")

        r = Rectangle(5, 10, 2, 3)
        r.y = 5
        self.assertEqual(r.y, 5)

        with self.assertRaises(ValueError):
            r.y = -10
        with self.assertRaises(TypeError):
            r.y = 3.4
        with self.assertRaises(TypeError):
            r.y = True

    def testArea(self):
        r = Rectangle(10, 10)
        self.assertEqual(r.area(), 100)
        r.width = 6
        self.assertEqual(r.area(), 60)
        r.height = 6
        self.assertEqual(r.area(), 36)
    
#    def test_str(self):
#        r1 = Rectangle(6, 2)
#        expected = "[Rectangle] (1) 1/0 - 6/2"
#        self.assertEqual(str(r), expected)
