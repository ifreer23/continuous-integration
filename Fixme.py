#!/usr/bin/python3


def factorial(n):
    '''
    Returns the product of all numbers from 1 to n.

    '''

    result = 1

    for i in range(2, n+1):

        result *= i

    return result


def triangular(n):
    '''
    Returns the nth triangular number.

    The nth triangular number is the sum of all numbers from 1 to n.
    It is like the factorial, but uses addition instead of multiplication.

  '''
    result = 1

    for i in range(2, n+1):

        result += i

    return result
