#!/usr/bin/python3

""" Rectangle model """

from models.base import Base


class Rectangle(Base):
	"""
	This is the Rectangle class that inherits from Base
	"""
	__width = 0
	__height = 0
	__x = 0
	__y = 0

	def __init__(self, width, height, x=0, y=0, id=None):
		super().__init__(id)
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, value):
		if type(value) is not int:
			raise TypeError("width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self.__width = value

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, value):
		if type(value) is not int:
			raise TypeError("height must be an integer")
		if value <= 0:
			raise ValueError("height must be > 0")
		self.__height = value

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		if type(value) is not int:
			raise TypeError("x must be an integer")
		if value < 0:
			raise ValueError("x must be >= 0")
		self.__x = value

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, value: int):
		if type(value) is not int:
			raise TypeError("y must be an integer")
		if value < 0:
			raise ValueError("y must be >= 0")
		self.__y = value

	def area(self):
		"""
		This function returns the area of the rectangle
		"""
		return self.__width * self.__height

	def display(self):
		"""
		This function displays a rectangle as a sequence of '#'
		"""
		print("\n" * self.__y, f"{' ' * self.__x}{'#' * self.__width}\n" * self.__height, end="", sep="")

	def __str__(self):
		"""
		__str__
		Return the string representation of the rectangle
		"""
		return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

	def update(self, *args, **kwargs):
		"""
		This function updates the properties of the rectangle
		"""
		attributes = ["id", "width", "height", "x", "y"]
		for i in range(len(args)):
			setattr(self, attributes[i], args[i])
			if i == len(args) - 1:
				return

		for name, value in kwargs.items():
			setattr(self, name, value)
