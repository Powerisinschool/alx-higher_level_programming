#!/usr/bin/python3

import unittest
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
		self.assertEqual(r1.id, 4)
		self.assertEqual(r2.id, 5)
		self.assertEqual(r3.id, 12)

	def test_raises_error(self):
		self.assertRaises(TypeError, Rectangle, 10, "2")
		with self.assertRaises(ValueError):
			r = Rectangle(10, 2)
			r.width = -10
		with self.assertRaises(TypeError):
			r = Rectangle(10, 2)
			r.x = {}
		self.assertRaises(ValueError, Rectangle, 10, 2, 3, -1)
