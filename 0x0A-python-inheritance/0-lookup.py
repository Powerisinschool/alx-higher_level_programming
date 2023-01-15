#!/usr/bin/python3
'''This function returns a list containing all\
     the methods and attributes belonging to an object'''

def lookup(obj):
	'''Function returning list of all the methods belonging to an object'''
	return dir(obj)
