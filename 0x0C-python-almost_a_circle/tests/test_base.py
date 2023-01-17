#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_basic_program(self):
        pass

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
