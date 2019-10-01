"""
    File: zipper3.py
    Author: Kevin Falconett
    Purpose: provides zipper3() which creates one
             linked list using all of the nodes from
             three linked lists alternated, thus 
             "zippering" them
"""

from list_node import *

def zipper3(list1,list2,list3):
    """
        "zippers" three lists by merging them
        into one list containing all nodes from
        the three lists alternated

        Parameters:
            list1 (LinkedList): list to "zipper"
            list2 (LinkedList): second list to "zipper"
            list3 (LinkedList): third list to "zipper"

        Returns:
            (ListNode) - zippered, Linked list containing all
            the nodes from the three lists alternated
    """

    head = list1
    head2 = list2
    head3 = list3

    zippered = None
    zip_curr = None

    # these booleans are used to determine which
    # list not to use in the first iteration
    headFirst = False
    head2First = False
    head3First = False

    while head is not None or head2 is not None or head3 is not None:

        if zippered is None:
            if head is not None:
                zippered = head
                head = head.next
                zippered.next = None
                zip_curr = zippered
                headFirst = True
            elif head2 is not None:
                zippered = head2
                head2 = head2.next
                zippered.next = None
                zip_curr = zippered
                head2First = True
            elif head3:
                zippered = head3
                head3 = head3.next
                zippered.next = None
                zip_curr = zippered
                head3First = True
        else:
            # picks nodes from each list if they are not
            # empty
            if head is not None and not headFirst:
                zip_curr.next = head
                head = head.next
                zip_curr = zip_curr.next
                zip_curr.next = None

                head2First = False
                head3First = False

            if head2 is not None and not head2First:
                zip_curr.next = head2
                head2 = head2.next
                zip_curr = zip_curr.next
                zip_curr.next = None

                headFirst = False
                head3First = False

            if head3 is not None and not head3First:
                zip_curr.next = head3
                head3 = head3.next
                zip_curr = zip_curr.next
                zip_curr.next = None

                headFirst = False
                head2First = False
                
    return zippered

