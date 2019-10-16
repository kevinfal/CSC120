"""
    File: list_intersections.py
    Author: Kevin Falconett
    Purpose: Provides list_intersection(), which
             returns a Linked List with all of the
             nodes with shared values from two linked
             lists
"""

from list_node import *

def list_intersection(head1,head2):
    """
    Finds all of the nodes with the same value
    from head1 and head2
    :param head1: (ListNode) first List
    :param head2: (ListNode) second List
    :return: (ListNode) of all the nodes in
             both linked lists with same values
             (None) if there are no shared nodes
    """
    retval = None
    curr1 = head1
    curr2 = head2

    while curr1 is not None:
        while curr2 is not None:
            # if in both
            if curr1.val == curr2.val:
                added = curr1
                curr = curr.next
                added.next = None
                retval = add_node(retval,added)

            curr2 = curr.next
        curr = curr.next
    return retval

def find_tail(head):
    """
    Gets the last node of a Linked List
    :param head: (ListNode) linked list to traverse
    :return: (ListNode) Last node of a Linked List
    """
    if head is None:
        return head
    elif head.next is None:
        return head
    else:
        return find_tail(head.next)

def add_node(head: ListNode, added: ListNode):
    """
    Adds a node to the end of a linked list
    :param head: (ListNode) Linked list to add to
    :param added: (ListNode) Node to add to list
    :return: (ListNode) with all Nodes in head with added at
             the end
    Precondition:
        Added.next must be none, or else may not function properly
    """
    if head is None:
        return added
    else:
        tail = find_tail(head)
        tail.next = added
        return head
