#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_lists(self):
        list1 = [3, 89, 55, 0]
        self.assertEqual(max_integer(list1), 89)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -56, 0, -100]), 0)
        self.assertEqual(max_integer([1, 2, 3, 4]), 3)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([1.3, 0.66, 6.1, -1.9]), 6.1)

    def test_string(self):
        self.assertEqual(max_integer('abcd'), 'd')
        self.assertEqual(max_integer('zebra'), 'z')
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer(['hello', 'world']), 'world')


if __name__ == '__main__':
    unittest.main()
