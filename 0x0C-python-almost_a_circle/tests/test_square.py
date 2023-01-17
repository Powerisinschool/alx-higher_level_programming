#!/usr/bin/python3

import unittest
import re
from models.square import Square


class TestBase(unittest.TestCase):
    def test_basic_program(self):
        pass

    def test_private_variable(self):
        with self.assertRaises(AttributeError):
            print(Square.__nb_objects)

    def test_string_repr(self):
        s1 = Square(5)
        self.assertEqual(str(s1), f"[Square] ({s1.id}) 0/0 - 5")
        s2 = Square(2, 2)
        self.assertEqual(str(s2), f"[Square] ({s2.id}) 2/0 - 2")
        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), f"[Square] ({s3.id}) 1/3 - 3")

    def test_raises_error(self):
        s1 = Square(5)
        with self.assertRaises(TypeError):
            s1.size = "9"
        with self.assertRaises(ValueError):
            s1.size = -10

    def test_dict_repr(self):
        s1 = Square(10, 2, 1)
        expected = {'id': s1.id, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1.to_dictionary(), expected)
        self.assertEqual(type(s1.to_dictionary()), dict)
