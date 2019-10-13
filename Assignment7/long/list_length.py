"""
    File: list_length.py
    Author: Kevin Falconett
    Purpose: provides function list_length() that traverses
             a linked list recursively and returns the length
"""

from list_node import *

def list_length(head):
    """
    traverses linked list recursively and
    returns the length
    :param head:
    :return:
    """
    if head is None:
        return 0
    else:
        length = 1
        return length + list_length(head.next)
