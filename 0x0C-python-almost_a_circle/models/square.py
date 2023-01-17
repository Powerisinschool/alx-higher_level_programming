#!/usr/bin/python3

""" Square model """

from models.rectangle import Rectangle


class Square(Rectangle):
	"""
	This is the square class that inherits from Rectangle
	"""
	def __init__(self, size, x=0, y=0, id=None):
		super().__init__(size, size, x, y, id)

	def __str__(self):
		"""
		__str__
		Return the string representation of the square
		"""
		return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
