"""
    File: insertion_sort.py
    Author: Kevin Falconett
    Purpose: Provides insertion sort for
             linked lists
"""

from list_node import *


def insertion_sort(head: ListNode):
    """
        Sorts a linked list in descending order

        Parameters:
            head (ListNode): front of linked list to sort
        
        Returns:
            (ListNode) - all elements in head sorted in
                         descending order
    """

    new = None  # sorted list

    while head is not None:

        print("head: ", head)
        print("new: ", new, "\n")

        curr_element = head
        head = head.next  # "removes" from unnew list
        curr_element.next = None

        if new is None or new.val < curr_element.val:
            # new is empty or curr greater than new
            # makes curr the new front of new

            added = curr_element
            curr_element = curr_element.next
            added.next = new
            new = added
        else:
            E = new
            while E is not None:
                if E.val >= curr_element.val and (
                    E.next == None or E.next.val < curr_element.val
                ):
                    # Element is greater than curr
                    # and its next is less than curr
                    # and inserts

                    next = E.next
                    E.next = curr_element
                    curr_element.next = next
                E = E.next

    print("head: ", head)
    print("new: ", new, "\n")

    return new


def main():
    """
        Used to test the functionality of
        insertion_sort(), creates a linked
        list and sorts it

        Linked list can be changed to test
        whatever possibility
    """
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)

    result = insertion_sort(node)
    print(result)


if __name__ == "__main__":
    main()
