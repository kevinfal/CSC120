'''
    File: reverse_list.py
    Author: Kevin Falconett
    Purpose: reverses a linked list
'''

from list_node import *


def reverse_list(head: ListNode):
    
    new = None
    
    while head is not None:
        
        current = head
        prev = current
        while current is not None:
            prev = current
            new = prev
            print(prev)
            
            current = current.next
            head = current
        head = current

    print("head: {}".format(head))
    print("new: {}".format(new))

    return new

def main():
    
    head = ListNode('a')
    head.next = ListNode('b')
    head.next.next = ListNode('c')

    print(reverse_list(head))

if __name__ == '__main__':
    main()