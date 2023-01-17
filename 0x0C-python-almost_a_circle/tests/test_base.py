#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_basic_program(self):
        pass

    def test_id_None(self):
        """ """
        b1 = Base(None)
        b2 = Base(None)
        b3 = Base(None)
        b4 = Base(None)
        self.assertEqual(b1.id, b1.id)
        self.assertEqual(b2.id, b1.id + 1)
        self.assertEqual(b3.id, b1.id + 2)
        self.assertEqual(b4.id, b1.id + 3)

    def test_id_string(self):
        """ """
        b1 = Base("Holberton")
        b2 = Base("School")
        b3 = Base("98")
        b4 = Base("")
        self.assertEqual(b1.id, "Holberton")
        self.assertEqual(b2.id, "School")
        self.assertEqual(b3.id, "98")
        self.assertEqual(b4.id, "")

    def test_id_Negative(self):
        """ """
        b1 = Base(-12)
        b2 = Base(-1)
        b3 = Base(-98)
        b4 = Base(-1024)
        self.assertEqual(b1.id, -12)
        self.assertEqual(b2.id, -1)
        self.assertEqual(b3.id, -98)
        self.assertEqual(b4.id, -1024)

    def test_id_float(self):
        """ """
        b1 = Base(12.5)
        b2 = Base(1.5)
        b3 = Base(98.5)
        b4 = Base(1024.5)
        self.assertEqual(b1.id, 12.5)
        self.assertEqual(b2.id, 1.5)
        self.assertEqual(b3.id, 98.5)
        self.assertEqual(b4.id, 1024.5)

    def test_private_variable(self):
        try:
            print(Base.__nb_objects)
        except AttributeError as e:
            self.assertIs(type(e), AttributeError)

    def test_functionality(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)

    def test_to_json_dict(self):
        dictionary = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        self.assertEqual(Base.to_json_string(dictionary),
                         '{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}')

    def test_from_json(self):
        json_string = '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]'
        self.assertEqual(len(Base.from_json_string(json_string)), 2)
