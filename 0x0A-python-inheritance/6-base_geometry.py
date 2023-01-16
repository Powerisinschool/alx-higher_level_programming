#!/usr/bin/python3

"""This class is a class"""


class BaseGeometry:
	"""
	This class contains the area method that raises an exception with the message area() is not implemented
	"""
	def area(self):
		"""
		This method raises an exception with the message area() is not implemented
		"""
		raise Exception("area() is not implemented")
