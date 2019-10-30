"""
    File: triangle2.py
    Author: Kevin Falconett
    Purpose: provides triangle2(), sum_num(), and fill()
"""

def triangle2(n):
    """
    Constructs a "triangle" with elements that count up
    :param n: the length of the triangle
    :return: List[][] -  a triangle of length n
    """

    # base case
    if n <= 0:
        return []
    else:
        returned = [fill(1 + sum_num(n -1),n)]
        returned = (triangle2(n-1)) + returned

        return returned

def sum_num(n):
    """
    Finds the natural sum of a number
    :param n: number to sum
    :return: (int) natural sum of a number
    """
    if n <= 1:
        return n
    else:
        return n + sum_num(n - 1)


def fill(start, n):
    """
    fills a part of the triangle
    :param start: number to start
    :param n: length of the part of the triangle
    :return: a List of length n that counts up from start
    """
    if n <= 0:
        return []
    else:
        returned = [start]
        returned.extend(fill(start + 1, n - 1))
        
        return returned
