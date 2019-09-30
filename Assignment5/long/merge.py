"""
    File: merge.py
    Author: Kevin Falconett

"""

from list_node import *

def merge(list1: ListNode,list2: ListNode):
    """

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
    l2 = ListNode(111)
    merged = None
    
    result = insert(None,l1)
    result = insert(result,l2)
    print(result)

if __name__ == '__main__':
    main()