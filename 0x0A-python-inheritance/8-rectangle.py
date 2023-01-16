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
		if value <= 0:
			raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
	"""
	This class inherits from BaseGeometry and creates a rectangle with width and height
	"""
	def __init__(self, width, height):
		"""
		Initialize the width and height of the rectangle, width and height must be positive integers
		"""
		self.__width = width
		self.__height = height
		self.integer_validator("width", self.__width)
		self.integer_validator("height", self.__height)
