"""
    File: list_intersections.py
    Author: Kevin Falconett
"""

from list_node import *

def list_intersection(head1,head2):
    """

    :param head1:
    :param head2:
    :return:
    """
    retval = None
    retCurr = None

    curr1 = head1
    curr2 = head2

    while curr1 is not None:
        while curr2 is not None:
            # if in both
            if curr1.val == curr2.val:
                added = curr1
                curr = curr.next
                added.next = None
                retval = insert(retval,added)


            curr2 = curr.next
        curr = curr.next
    return retval

def insert(head: ListNode, added: ListNode):
    '''
        Inserts a node (added) into a linked
        list (head) in the order its proper position
        (descending)

        Parameters:
            head (ListNode): Linked List/node of list to add to
            added (ListNode): node to be added

        Returns:
            (ListNode) - E, linked list/node with added inserted
            into its proper location in the list (heaad)

        Preconditions:
            added.next should be of type (None)

    '''
    E = head
    if head is None:
        return added
    elif E is None or E.val < added.val:
        # E is empty or added greater than E
        # makes added the new front of E

        added.next = head
        E = added
    else:
        curr = E
        while curr is not None:

            # Element is greater than curr
            # and its next is less than curr
            # and inserts
            if curr.val > added.val and (curr.next == None
                                          or curr.next.val < added.val):
                next = curr.next
                curr.next = added
                added.next = next
            curr = curr.next
    return E


def main():
    pass

if __name__ == '__main__':
    main()