#!/usr/bin/python3

""" Student module """


class Student:
	"""
	This class is defined for a student
	"""
	def __init__(self, first_name, last_name, age):
		"""
		Initialize a new Student instance

		:param first_name: string
		:param last_name: string
		:param age: int
		"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def to_json(self, attrs=None):
		"""
		Returns a dictionary representation of a Student instance

		:return: dictionary
		"""
		if attrs is None:
			return self.__dict__
		else:
			return {k: v for k, v in self.__dict__.items() if k in attrs}
