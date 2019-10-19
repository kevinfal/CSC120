"""
    File: dl_insert.py
    Author: Kevin Falconett
"""

from dlist_node import *

def dl_insert_before(head, node_in_list, node_to_insert):

    
    curr = head
    while curr is not None:
        if curr.get_val() == node_in_list.get_val():
            
            if curr.get_prev() is not None:
                
                prev = curr.get_prev()
                prev.set_next(node_to_insert)
                node_to_insert.set_prev(prev)
                node_to_insert.set_next(curr)
                curr.set_prev(node_to_insert)
            else:
                head = node_to_insert
                node_to_insert.set_next(curr)
                node_to_insert.set_prev(None)
                curr.set_prev(node_to_insert)
                return head
                
            return head
        curr = curr.get_next()
    return head
            
def dl_insert_after(head: DListNode, node_in_list, node_to_insert: DListNode):
    curr = head
    while curr is not None:
        if curr.get_val() == node_in_list.get_val():

            if curr.get_next() is None:
                curr.set_next(node_to_insert)
                node_to_insert.set_prev(curr)

            else:
                prev = curr
                mid = node_to_insert
                after = curr.get_next()
                after.set_prev(mid)
                mid.set_next(after)
                mid.set_prev(prev)
                prev.set_next(mid)
            return head
        curr = curr.get_next()
    return head

def test_before():
    print("inserting before")
    a = DListNode(5)
    a = dl_insert_before(a,a, DListNode(4))
    a = dl_insert_before(a, DListNode(4), DListNode(3))
    a = dl_insert_before(a, DListNode(3),DListNode(2))
    a = dl_insert_before(a,DListNode(3), DListNode(7))
    
    print(str(a.get_prev()) +str(a))

def test_after():
    print("Inserting after")
    a = DListNode(5)
    a = dl_insert_after(a,a, DListNode(4))
    a = dl_insert_after(a, DListNode(4), DListNode(3))
    a = dl_insert_after(a, DListNode(3),DListNode(2))
    
    print(str(a.get_prev()) +str(a))


def main():
    test_before()
    test_after()


if __name__ == "__main__":
    main()