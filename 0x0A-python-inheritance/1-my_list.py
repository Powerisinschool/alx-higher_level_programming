#!/usr/bin/python3

class MyList(list):
	"""
    This class inherits from the built-in list class and has a public instance method print_sorted
    """
	def print_sorted(self):
		"""
        This method prints the list in ascending order
        """
		print(sorted(self))
		