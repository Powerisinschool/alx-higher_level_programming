#!/usr/bin/python3
'''Square Class

A Square Class

'''


class Square:
    '''Square with size'''

    def __init__(self, size=0):
        '''__init__

        The __init__ method initializes the size method of the square.

        Attributes:
            size (:obj:'int', optional): The size of the square

        Raises:
            TypeError: If 'size' type is not an integer

            ValueError: if 'size' < 0
        '''

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        '''Returns the current square area'''
        return self.__size ** 2

    def my_print(self):
        '''Prints the square with the character #'''
        if self.__size == 0:
            print()
        else:
            i, j = 1, 1
            for i in range(self.__size):
                length = ''
                for j in range(self.__size):
                    length += '#'
                    j += 1
                print(length)
                i += 1
