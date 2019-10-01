"""
    File: merge.py
    Author: Kevin Falconett
    Purpose: Provides merge() which takes
             two linked lists/nodes and merges
             them into a single list ordered
"""

from list_node import *

def merge(list1: ListNode,list2: ListNode):
    """
        Merges list 1 and list two into one
        sorted linked list
        
        Parameters:
            list1 (ListNode): head node of a linked list
            list2 (ListNode): head node of second linked list
        Returns:
            (ListNode) - linked list/node that hold all
            values in list1 and list2 ordered
        Preconditions:
            none

    """
    head = list1
    head2 = list2
    merged = None
    # inserts everything from list1 into merged first
    while head is not None:
        added = head
        head = head.next
        added.next = None
        merged = insert(merged,added)
    # then inserts everything from list2
    while head2 is not None:
        added = head2
        head2 = head2.next
        added.next = None
        merged = insert(merged,added)
    return merged

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
            if curr.val >= added.val and (
                curr.next == None or curr.next.val < added.val):
                # Element is greater than curr
                # and its next is less than curr
                # and inserts

                next = curr.next
                curr.next = added
                added.next = next
            curr = curr.next
    return E

def main():
    """
        Function to test the functionality of merge()
        Linked lists are provided and can be changed to
        test several cases
    """
    l1 = ListNode(222)
    l1.next = ListNode(444)
    l2 = ListNode(111)
    l2.next = ListNode(333)
    merged = merge(l1,l2)
    
    print(merged)

if __name__ == '__main__':
    main()