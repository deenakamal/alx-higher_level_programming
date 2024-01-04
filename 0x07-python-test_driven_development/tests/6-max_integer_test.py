#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    unittest for max_integer function.
    """

    def test_normal_list(self):
        """unittest for normal case """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        """unittest for empty list """
        self.assertIsNone(max_integer([]))

    def test_negative_list(self):
        """unittest for list containes negative number"""
        self.assertEqual(
            max_integer([-23, 58, 91, 24, -1024, 89, 98, 108]), 108)

    def test_type_error(self):
        """unittest for raise type error"""
        with self.assertRaises(TypeError):
            max_integer([90, "m"])

    def test_none_input(self):
        """unittest for raise error"""
        with self.assertRaises(TypeError):
             max_integer(None)

    def test_single_element_list(self):
        """ unittest for single element in list"""
        self.assertEqual(max_integer([42]), 42)

if __name__ == '__main__':
    unittest.main()
