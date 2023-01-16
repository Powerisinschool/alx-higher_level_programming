#!/usr/bin/python3

""" Pascal Triangle module """


def factorial(n: int):
	"""
	This function returns the factorial of a number
	:param n: int
	:return: The factorial (int)
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)


def pascal_triangle(n: int):
	"""
	This function returns a list of lists of integers representing the Pascal’s triangle of n

	:param n: int
	:return: list of lists
	"""
	triangle = []

	if n <= 0:
		return triangle

	for i in range(n):
		triangle.append([])
		for k in range(i+1):
			triangle[i].append(int(factorial(i) / (factorial(k) * factorial(i-k))))

	return triangle
