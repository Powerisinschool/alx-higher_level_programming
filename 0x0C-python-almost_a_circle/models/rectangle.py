#!/usr/bin/python3

""" Rectangle model """

import base


class Rectangle(base.Base):
	"""
	This is the Rectangle class that inherits from Base
	"""

	def __init__(self, width, height, x=0, y=0, id=None):
		super().__init__(id)
		self.__width = width
		self.__height = height
		self.__x = x
		self.__y = y

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, value: int):
		self.__width = value

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, value: int):
		self.__height = value

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value: int):
		self.__x = value

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, value: int):
		self.__y = value
