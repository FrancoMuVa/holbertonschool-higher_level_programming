#!/usr/bin/python3
import io
import unittest
from unittest.mock import patch
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

    def testStr(self):
        r1 = Rectangle(6, 2, 7, 10, 2)
        expected = "[Rectangle] (2) 7/10 - 6/2"
        self.assertEqual(str(r1), expected)

    def testDisplay(self):
        r1 = Rectangle(4, 2)
        expected = "####\n####"
        with patch("sys.stdout", new_callable=io.StringIO) as output:
            r1.display()
            self.assertEqual(output.getvalue().strip(), expected)

    def testUpdate(self):
        r1 = Rectangle(2, 5, 12, 2, 8)

        r1.update(4)
        self.assertEqual(r1.id, 4)

        r1.update(4, 8)
        self.assertEqual(r1.width, 8)

        r1.update(4, 8, 10)
        self.assertEqual(r1.height, 10)

        r1.update(4, 8, 10, 7)
        self.assertEqual(r1.x, 7)

        r1.update(4, 8, 10, 7, 3)
        self.assertEqual(r1.y, 3)

    def testToDictionary(self):
        r1 = Rectangle(5, 7, 4, 3, 10)
        espected = {"id": 10, "width": 5, "height": 7, "x": 4, "y": 3}
        self.assertEqual(r1.to_dictionary(), espected)
