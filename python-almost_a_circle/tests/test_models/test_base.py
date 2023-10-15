#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def testToJsonString(self):
        self.assertEqual(Base.to_json_string([]), "[]")

        list_of_dicts = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]
        expected = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(Base.to_json_string(list_of_dicts), expected)
    
    def testSaveToFile(self):
        r1 = Rectangle(2, 4, 2, 2, 1)
        expected = '[{"id": 1, "width": 2, "height": 4, "x": 2, "y": 2}]'
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            rectangle_json = f.read()
            self.assertEqual(rectangle_json, expected)

        s1 = Square(3, 2, 2, 3)
        expected = '[{"id": 3, "size": 3, "x": 2, "y": 2}]'
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            square_json = f.read()
            self.assertEqual(square_json, expected)

    def testFromJsonString(self):
        string = '[{"id": 2, "size": 3, "x": 0, "y": 0}]'
        json_list = Base.from_json_string(string)
        expected = [{"id": 2, "size": 3, "x": 0, "y": 0}]
        self.assertEqual(json_list, expected)

    def testCreate(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def testIDCreate(self):
        b3 = Base(9)
        self.assertEqual(b3.id, 9)

    def testCreateRectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)

        self.assertEqual(r2.id, 4)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)

    def testCreateSquare(self):
        s1 = Square(3, 1, 2, 1)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 3)
    
    def testLoadFromFileExist(self):
        with open("Square.json", "w") as f:
            f.write('[{"id": 1, "size": 5}, {"id": 2, "size": 8}]')

        list_instances = Square.load_from_file()

        self.assertEqual(len(list_instances), 2)

        self.assertEqual(list_instances[0].id, 1)
        self.assertEqual(list_instances[0].size, 5)

        self.assertEqual(list_instances[1].id, 2)
        self.assertEqual(list_instances[1].size, 8)


    def testLoadFromFile(self):
        instances_list = Base.load_from_file()
        self.assertEqual(len(instances_list), 0)
