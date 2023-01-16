#!/usr/bin/python3

""" This class is a class """


class MyInt(int):
	"""
	This class inherits from int and overrides the == and != operators
	"""
	def __eq__(self, value):
		"""
		Override the == operator to invert the logic
		"""
		return super().__ne__(value)

	def __ne__(self, value):
		"""
		Override the != operator to invert the logic
		"""
		return super().__eq__(value)
