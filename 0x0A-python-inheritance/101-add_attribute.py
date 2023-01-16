#!/usr/bin/python3

def add_attribute(obj, name, value):
	"""
	This function adds a new attribute to an object if it's possible
	"""
	if not hasattr(obj, '__setattr__') or type(obj) in (str, tuple, int, float, bool):
		raise TypeError("can't add new attribute")
	setattr(obj, name, value)
