#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_unordered_list(self):
        """ Test max integer in a unordered list """
        unordered = [1, 4, 2, 7]
        self.assertEqual(max_integer(unordered), 7)

    def test_sorted_list(self):
        """ Test max integer in a sorted list """
        sorted = [1, 2, 3, 4, 5, 6]
        self.assertEqual(max_integer(sorted), 6)

    def test_sorted_rev(self):
        rev = [6, 5, 4, 3, 2, 1]
        """ Test max integer in a reversed list """
        self.assertEqual(max_integer(rev), 6)

    def test_no_integers(self):
        """ Test max integer in a list without integers """
        list = ["Hello", "my", "name", "is", "Franco"]
        self.assertEqual(max_integer(list), "name")

    def test_string(self):
        """ Test a string """
        string = "Franco Musso"
        self.assertEqual(max_integer(string), "u")
    
    def test_empty_list(self):
        """ Test max integer (empty list) """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_single_num(self):
        """ Test max integer in a list with a single number """
        single = [1024]
        self.assertEqual(max_integer(single), 1024)
    
    def test_single_char(self):
        """ Test max integer in a string with single char """
        s_char = "F"
        self.assertEqual(max_integer(s_char), "F")

    def test_negative(self):
        """ Test max integer in a list with negative numbers """
        negative_list = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(negative_list), -1)
    
    def test_float(self):
        """ Test max integer in a list with float numbers """
        list_float = [1.45, 5.32, 3.0, 35.4, -3.3]
        self.assertEqual(max_integer(list_float), 35.4)

    def test_int_float(self):
        """ Test max integer in a list with float and integers numbers """
        int_float = [1, 5.90, 4.8, -3, 100, 100.1]
        self.assertEqual(max_integer(int_float), 100.1)

if __name__ == '__main__':
    unittest.main()
