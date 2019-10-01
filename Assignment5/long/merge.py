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
            

    """
    
    head = list1
    head2 = list2
    merged = None
    while head is not None:
        added = head
        head = head.next
        added.next = None
        merged = insert(merged,added)
    while head2 is not None:
        added = head2
        head2 = head2.next
        added.next = None
        merged = insert(merged,added)
    return merged

def insert(head, added):
    E = head
    if head is None:
        return added
    elif E is None or E.val < added.val:
            # new is empty or curr greater than new
            # makes curr the new front of new
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
    l1 = ListNode(222)
    l1.next = ListNode(444)
    l2 = ListNode(111)
    l2.next = ListNode(333)
    merged = merge(l1,l2)
    
    print(merged)

if __name__ == '__main__':
    main()