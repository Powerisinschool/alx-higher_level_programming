#!/usr/bin/python3
'''Square Class

A Square Class

'''


class Square:
    '''Square with size'''

    def __init__(self, size=0, position=(0, 0)):
        '''__init__

        The __init__ method initializes the size method of the square.

        Attributes:
            size (:obj:'int', optional): The size of the square
            position (:obj:'int', optional): The position of the square

        Raises:
            TypeError: If 'size' type is not an integer

            ValueError: if 'size' < 0
        '''

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (type(position) is not tuple
                or type(position[0]) is not int
                or type(position[1]) is not int
                or position[0] < 0
                or position[1] < 0
                or len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple
                or type(value[0]) is not int
                or type(value[1]) is not int
                or value[0] < 0
                or value[1] < 0
                or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        '''Returns the current square area'''
        return self.__size ** 2

    def my_print(self):
        '''Prints the square with the character #'''
        if self.__size == 0:
            print()
            return None

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')

        for j in range(1, self.area() + 1):
            if j % self.__size == 1:
                print('{:>{w}}'.format('#', w=self.__position[0] + 1), end='')
            else:
                print('#', end='')

            if j % self.__size == 0 and j > 0:
                print()
