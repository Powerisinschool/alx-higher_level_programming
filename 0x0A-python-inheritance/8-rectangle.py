#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""This class is a class"""


class Rectangle(BaseGeometry):
	__width = 0
	__height = 0

	def __init__(self, width, height):
		BaseGeometry.integer_validator(self, "width", width)
		BaseGeometry.integer_validator(self, "height", height)
		self.__width = width
		self.__height = height
