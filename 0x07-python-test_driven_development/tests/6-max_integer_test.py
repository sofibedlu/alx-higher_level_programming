#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        list1 = [3, 89, 55, 0]
        self.assertEqual(max_integer(list1), 89)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -56, 0, -100]), 0)


if __name__ == '__main__':
    unittest.main()
