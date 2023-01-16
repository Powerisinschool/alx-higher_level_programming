#!/usr/bin/python3

def add_attribute(obj, name, value):
	if not hasattr(obj, '__setattr__') or type(obj) in (str, tuple, int, float, bool):
		# print(obj)
		raise TypeError("can't add new attribute")
	setattr(obj, name, value)
