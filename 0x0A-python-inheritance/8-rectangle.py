#!/usr/bin/python3

"""This class is a class"""


class BaseGeometry:
	"""
	This is an empty class
	"""
	def area(self):
		raise Exception("area() is not implemented")

	def integer_validator(self, name, value):
		if type(value) is not int:
			raise TypeError(f"{name} must be an integer")
		elif value <= 0:
			raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
	__width = 0
	__height = 0

	def __init__(self, width, height):
		BaseGeometry.integer_validator(self, "width", width)
		BaseGeometry.integer_validator(self, "height", height)
		self.__width = width
		self.__height = height
