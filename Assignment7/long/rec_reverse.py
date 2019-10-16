"""
    File: rec_reverse.py
    Author: Kevin Falconett
    Purpose: provides rec_reverse() which reverses a
    linked list recursively
"""

from list_node import *


def rec_reverse(head):
    """
    Reverses a Linked List
    :param head:
    :return:
    """
    # empty
    if head is None:
        return None
    # if last node/length is one
    elif head.next is None:
        return head
    else:
        # this is the "new" list
        returned = rec_reverse(head.next)
        # here head looks like head -> next -> None
        head.next.next = head
        # setting head.next so it doesn't point to node moved
        head.next = None

        return returned


def main():
    """
        Tests functionality for rec_reverse, constructs
        linked list, prints before reverse and after
    """
    n = ListNode(0)
    curr = n
    for x in range(1,6):
        curr.next = ListNode(x)
        curr = curr.next
    print(n)
    print(rec_reverse(n))


if __name__ == '__main__':
    main()