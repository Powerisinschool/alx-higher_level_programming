#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
	def test_basic_program(self):
		pass

	def test_private_variable(self):
		# self.assertRaises(AttributeError, print(Base.__nb_objects))
		pass
