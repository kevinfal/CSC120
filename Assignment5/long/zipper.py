"""
    File: zipper.py
    Author: Kevin Falconett

"""

from list_node import *

def zipper(list1,list2):


    zippered = None
    head = list1
    head2 = list2
    zip_curr = None
    use_list1 = True

    if head is None and head2 is None:
        return None
    if head is None:
        return head2
    elif head2 is None:
        return head

    while head is not None and head2 is not None:

        if zippered is None:
            zippered = head
            head = head.next
            zippered.next = None
            zip_curr = zippered
            use_list1 = False
        
        if not use_list1 and head2 is not None:
            zip_curr.next = head2
            head2 = head2.next

            zip_curr = zip_curr.next
            zip_curr.next = None
            use_list1 = True

        if use_list1 and head is not None:
            zip_curr.next = head
            head = head.next
            
            zip_curr = zip_curr.next
            zip_curr.next = None
            use_list1 = False
    
    

    if head is None:
        zip_curr.next = head2
    elif head2 is None:
        zip_curr.next = head

    return zippered
           
                    
        


def main():
    
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