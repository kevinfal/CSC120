"""
    File: sum_lists.py
    Author: Kevin Falconett

"""

from list_node import *

def sum_lists(list1,list2):
    
    head = list1
    head2 = list2
    sum_list = None

    if head is None:
        return head2
    elif head2 is None:
        return head

    sum_curr = sum_list

    while head is not None:
        node1 = head
        head = head.next
        node2 = head2
        head2 = head2.next
        
        sum = ListNode(node1.val + node2.val)

        if sum_curr is None:
            sum_list = sum
            sum_curr = sum_list
        else:
            sum_curr.next = sum
            sum_curr = sum_curr.next

    while head2 is not None:
        node = head2
        head2 = head2.next

        sum_curr.next = node
        sum_curr = sum_curr.next

    

    return sum_list
        
        

def main():
    
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)

    l2 = ListNode(1)
    l2.next = ListNode(2)
    l2.next.next = ListNode(3)
    l2.next.next.next = ListNode(4)

    result = sum_lists(l1,l2)
    print(result)

if __name__ == '__main__':
    main()