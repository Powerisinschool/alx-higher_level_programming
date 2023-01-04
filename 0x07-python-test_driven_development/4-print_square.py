#!/usr/bin/python3
'''Function that prints a square with the character #'''


def print_square(size):
    '''This function prints a square'''
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif type(size) is float and size < 0:
        raise ValueError('size must be am integer')
    for s in range(1, size+1):
        print('#'*size, end='\n')
