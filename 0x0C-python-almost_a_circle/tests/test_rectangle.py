#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
	def test_basic_program(self):
		pass

	def test_private_variable(self):
		try:
			print(Rectangle.__nb_objects)
		except AttributeError as e:
			self.assertIs(type(e), AttributeError)

	def test_functionality(self):
		r1 = Rectangle(10, 2)
		r2 = Rectangle(2, 10)
		r3 = Rectangle(10, 2, 0, 0, 12)
		self.assertEqual(r1.id, 4)
		self.assertEqual(r2.id, 5)
		self.assertEqual(r3.id, 12)
