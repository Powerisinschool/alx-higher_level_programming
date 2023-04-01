#!/usr/bin/python3
""" function find_peak """


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    a = list_of_integers
    for i in range(1, len(a)):
        if i == len(a)-1:
            return a[i] if a[i] >= a[i-1] else None
        if (a[i] >= a[i-1] and i > 1) and (a[i] >= a[i+1] and i < len(a)):
            return a[i]
    if a[0] >= a[1]:
        return a[0]
