#!/usr/bin/python3
import sys

if __name__ == '__main__':
    '''
    Prints the number of and list of arguments
    '''

    av = sys.argv
    l_av = len(av) - 1
    sum = 0

    if l_av >= 1:
        for i in range(1, l_av + 1):
            sum += int(av[i])
        print(sum)
    elif l_av == 0:
        print(sum)
