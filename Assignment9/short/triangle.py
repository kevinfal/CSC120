"""
    File: triangle.py
    Author: Kevin Falconett
"""

def triangle(length, value):
    if length <= 0:
        return []
    else:
        returned = [[value] * length]
        returned = triangle(length - 1, value) + returned
        return returned
