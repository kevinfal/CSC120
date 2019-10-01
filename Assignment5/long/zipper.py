"""
    File: zipper.py
    Author: Kevin Falconett
    Purpose: provides zipper() which merges two
             Linked lists into one list containing
             each element in both lists alternated
"""

from list_node import *

def zipper(list1,list2):
    """
        merges two linked lists into a single list
        containing each element of both lists alternated
        thus "zippering" it

        Parameters:
            list1 (ListNode): Linked List/node to be "zippered"
            list2 (ListNode): second Linked List/node to "zipper"
        
        Returns:
            (ListNode) - zippered, contains each element of list1
            and list2 alternated, if one list runs out early it uses
            the rest of the other list
        
        Preconditions:
            None
    """

    zippered = None
    head = list1
    head2 = list2
    zip_curr = None
    use_list1 = True  # flag to determine which list to use

    if head is None and head2 is None:
        return None
    if head is None:
        return head2
    elif head2 is None:
        return head

    while head is not None and head2 is not None:

        # first iteration
        if zippered is None:
            zippered = head
            head = head.next
            zippered.next = None
            zip_curr = zippered
            use_list1 = False
        
        # use second list if not none
        if not use_list1 and head2 is not None:
            zip_curr.next = head2
            head2 = head2.next

            zip_curr = zip_curr.next
            zip_curr.next = None
            use_list1 = True
            
        # use first list if not none
        if use_list1 and head is not None:
            zip_curr.next = head
            head = head.next
            
            zip_curr = zip_curr.next
            zip_curr.next = None
            use_list1 = False
    
    # if one head is empty, use the rest of the other
    if head is None:
        zip_curr.next = head2
    elif head2 is None:
        zip_curr.next = head

    return zippered
           
                    
        


def main():
    """
        Used to test the functionality of zipper().
        Provides linked lists to test with, values can
        be changed
    """
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(5)

    list2 = ListNode(2)
    list2.next = ListNode(4)
    list2.next.next = ListNode(6)

    result = zipper(list1,list2)
    print(result)

if __name__ == "__main__":
    main()