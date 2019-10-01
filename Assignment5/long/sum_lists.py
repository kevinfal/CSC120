"""
    File: sum_lists.py
    Author: Kevin Falconett
    Purpose: provides sum_lists() which creates
             a new linked list that contains the sum
             of each corresponding nodes of 2 linked lists
"""

from list_node import *

def sum_lists(list1,list2):
    """
        Takes two linked lists/nodes and creates
        a linked list with each node containing the
        sum of the two lists' corresponding nodes.
        
        Parameters:
            list1 (ListNode): first list to sum
            list2 (ListNode): second list to sum

        Returns:
            (ListNode) sum_list, a Linked list containing the
            sums of list1 and list2's corresponding values.
            When one is longer than the other, the list will contain
            the rest of the nodes in the longer list

        Preconditinos:
            All nodes in list1 and list2 have values that can be added
            (i.e str,int)
    """
    
    head = list1
    head2 = list2
    sum_list = None

    if head is None:
        return head2
    elif head2 is None:
        return head

    sum_curr = sum_list

    while head is not None:

        # crate corresponding nodes
        node1 = head
        head = head.next
        node2 = head2
        head2 = head2.next
        
        # create node to add
        sum = ListNode(node1.val + node2.val)

        # if first iteration
        if sum_curr is None:
            sum_list = sum
            sum_curr = sum_list
        else:
            sum_curr.next = sum
            sum_curr = sum_curr.next

    # iterate through head2 and move values to sum_list
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