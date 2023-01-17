#!/usr/bin/python3

import unittest
import re
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_basic_program(self):
        pass

    def test_private_variable(self):
        with self.assertRaises(AttributeError):
            print(Rectangle.__nb_objects)

    def test_functionality(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(12, 2)
        self.assertEqual(r2.id, r1.id + 1)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, r1.id + 2)

    def test_raises_error(self):
        self.assertRaises(TypeError, Rectangle, 10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        self.assertRaises(ValueError, Rectangle, 10, 2, 3, -1)

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_string_representation(self):
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1))[-9:], "1/0 - 5/5")
        pattern = re.compile(r"\[Rectangle] \([0-9]+\) 1/0 - 5/5")
        self.assertRegex(str(Rectangle(5, 5, 1)), pattern)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

        r1.update(90, 12, 23, 44, 35)
        self.assertEqual(r1.id, 90)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 23)
        self.assertEqual(r1.x, 44)
        self.assertEqual(r1.y, 35)

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)
