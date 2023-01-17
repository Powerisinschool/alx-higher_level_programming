#!/usr/bin/python3

import unittest
import re
from models.square import Square


class TestBase(unittest.TestCase):
    def test_basic_program(self):
        pass

    def test_square_size(self):
        """ """
        s1 = Square(10)
        s2 = Square(2, 0, 0, 12)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s2.size, 2)

    def test_square_x(self):
        """ """
        s1 = Square(10)
        s2 = Square(2, 0, 0, 12)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s2.x, 0)

    def test_square_y(self):
        """ """
        s1 = Square(10)
        s2 = Square(2, 0, 0, 12)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s2.y, 0)

    def test_square_area(self):
        """ """
        s1 = Square(3)
        s2 = Square(2, 0, 0, 12)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s1.area(), 9)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 64)

    def test_square_str(self):
        """ """
        s1 = Square(3)
        s2 = Square(2, 0, 0, 12)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s1.__str__(), f"[Square] ({s1.id}) 0/0 - 3")
        self.assertEqual(s2.__str__(), "[Square] (12) 0/0 - 2")
        self.assertEqual(s3.__str__(), "[Square] (12) 0/0 - 8")

    def test_square_update(self):
        """ """
        s1 = Square(10)
        s2 = Square(2, 0, 0, 12)
        s1.update(89)
        s2.update(89, 2, 0, 0)
        self.assertEqual(s1.__str__(), "[Square] (89) 0/0 - 10")
        self.assertEqual(s2.__str__(), "[Square] (89) 0/0 - 2")

    def test_square_update_args(self):
        """ """
        s1 = Square(10)
        s2 = Square(2, 0, 0, 12)
        s1.update(size=1)
        s2.update(size=1, x=2, y=2)
        self.assertEqual(s1.__str__(), f"[Square] ({s1.id}) 0/0 - 1")
        self.assertEqual(s2.__str__(), "[Square] (12) 2/2 - 1")

    def test_square_update_kwargs(self):
        """ """
        s1 = Square(10)
        s2 = Square(2, 0, 0, 12)
        s1.update(size=1, id=89)
        s2.update(size=1, x=2, y=2, id=89)
        self.assertEqual(s1.__str__(), "[Square] (89) 0/0 - 1")
        self.assertEqual(s2.__str__(), "[Square] (89) 2/2 - 1")

    def test_square_to_dict(self):
        """ """
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s1.__str__(), s2.__str__())
        self.assertNotEqual(s1, s2)

    def test_square_to_dict_none(self):
        """ """
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s1.__str__(), s2.__str__())
        self.assertNotEqual(s1, s2)

    def test_square_to_dict_args(self):
        """ """
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s1.__str__(), s2.__str__())
        self.assertNotEqual(s1, s2)

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
