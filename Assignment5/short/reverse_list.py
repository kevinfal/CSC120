'''
    File: reverse_list.py
    Author: Kevin Falconett
    Purpose: reverses a linked list
'''

from list_node import *


def reverse_list(head: ListNode):
    '''
        Reverses a linked list
    '''
    new = None

    while head is not None:
        print("head: ",head)
        print("new: ",new,"\n")
        current = head
        head = head.next
        current.next = new
        new = current

    print("head: ",head)
    print("new: ",new,"\n")

    return new

def main():
    
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)

    print(reverse_list(head))

if __name__ == '__main__':
    main()