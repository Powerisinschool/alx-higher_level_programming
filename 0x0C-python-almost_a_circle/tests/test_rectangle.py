#!/usr/bin/python3

import unittest
import re
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_basic_program(self):
        pass

    def test_rectangle_id(self):
        """ """
        r1 = Rectangle(10, 10)
        r2 = Rectangle(2, 4)
        r3 = Rectangle(3, 5, 0, 0, 12)
        self.assertEqual(r1.id, r1.id)
        self.assertEqual(r2.id, r1.id + 1)
        self.assertEqual(r3.id, 12)

    def test_rectangle_width(self):
        """ """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 4)
        r3 = Rectangle(3, 5, 0, 0, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r3.width, 3)

    def test_rectangle_height(self):
        """ """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 4)
        r3 = Rectangle(3, 5, 0, 0, 12)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r3.height, 5)

    def test_rectangle_x(self):
        """ """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 4)
        r3 = Rectangle(3, 5, 0, 0, 12)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r3.x, 0)

    def test_rectangle_y(self):
        """ """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 4)
        r3 = Rectangle(3, 5, 0, 0, 12)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.y, 0)

    def test_rectangle_str(self):
        """ """
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 4, 0, 0, 12)
        r3 = Rectangle(3, 5, 0, 0, 12)
        self.assertEqual(r1.__str__(), f"[Rectangle] ({r1.id}) 0/0 - 3/2")
        self.assertEqual(r2.__str__(), "[Rectangle] (12) 0/0 - 2/4")
        self.assertEqual(r3.__str__(), "[Rectangle] (12) 0/0 - 3/5")

    def test_rectangle_update(self):
        """ """
        r1 = Rectangle(10, 10, 10, 10)
        r2 = Rectangle(5, 5, 5, 5, 12)
        r1.update(89)
        r2.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        self.assertEqual(r2.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_rectangle_update_args(self):
        """ """
        r1 = Rectangle(10, 10, 10, 10)
        r2 = Rectangle(5, 5, 5, 5, 12)
        r1.update(89, 2, 3, 4, 5)
        r2.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        self.assertEqual(r2.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_rectangle_to_dict(self):
        """ """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertNotEqual(r1, r2)

    def test_rectangle_to_dict_none(self):
        """ """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertNotEqual(r1, r2)

    def test_rectangle_to_dict_args(self):
        """ """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertNotEqual(r1, r2)

    def test_private_variable(self):
        with self.assertRaises(AttributeError):
            print(Rectangle.__nb_objects)

    def test_functionality(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(12, 2)
        r5 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r2.id, r1.id + 1)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, r1.id + 2)
        self.assertEqual(r5.id, r1.id + 3)

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

    def test_string_repr(self):
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
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

    def test_dict_repr(self):
        r1 = Rectangle(10, 2, 1, 9)
        expected = {'id': r1.id, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r1.to_dictionary(), expected)
        self.assertEqual(type(r1.to_dictionary()), dict)
