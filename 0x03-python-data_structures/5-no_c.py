#!/usr/bin/python3
def no_c(my_string):
    list = []
    for element in my_string:
        list.append(element)
        while 'c' in list:
            list.remove('c')
        while 'C' in list:
            list.remove('C')
    return ''.join(list)
