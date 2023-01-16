#!/usr/bin/python3

"""This class is a class"""


def inherits_from(obj, a_class):
	"""
	This function checks if the object is an instance of a class that inherited (directly or indirectly)
	from the specified class.
	"""
	return issubclass(type(obj), a_class)
