#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = a / b
        return quotient
    except ValueError:
        quotient = None
        return quotient
    finally:
        print('Inside result: {}'.format(quotient))
