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
		if not self > value and not self < value:
			return False

	def __ne__(self, value):
		"""
		Override the != operator to invert the logic
		"""
		return not self == value
