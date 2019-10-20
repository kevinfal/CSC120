"""
    File: dl_insert.py
    Author: Kevin Falconett
    Purpose: provides dl_insert_before() and dl_insert_after() which
             insert before or after a specified node
"""

from dlist_node import *

def dl_insert_before(head, node_in_list, node_to_insert):
    """
    Inserts before a specified node
    :param head: head of list
    :param node_in_list: node that is in list
    :param node_to_insert: node to be added
    :return: list after modifications
    """
    curr = head
    while curr is not None:
        if curr.get_val() == node_in_list.get_val():
            
            if curr.get_prev() is not None:
                # Inserting at a node not head
                prev = curr.get_prev()
                prev.set_next(node_to_insert)
                node_to_insert.set_prev(prev)
                node_to_insert.set_next(curr)
                curr.set_prev(node_to_insert)
            else:
                #  Inserting at head
                head = node_to_insert
                node_to_insert.set_next(curr)
                node_to_insert.set_prev(None)
                curr.set_prev(node_to_insert)
                return head
                
            return head
        curr = curr.get_next()
    return head
            
def dl_insert_after(head: DListNode, node_in_list, node_to_insert: DListNode):
    """
    Inserts before a specified node
    :param head: head of list
    :param node_in_list: node that is in list
    :param node_to_insert: node to be added
    :return: list after modifications
    """
    curr = head
    while curr is not None:
        # node is the one we're looking for
        if curr.get_val() == node_in_list.get_val():
            # inserting at end of head
            if curr.get_next() is None:
                curr.set_next(node_to_insert)
                node_to_insert.set_prev(curr)

            else:
                # inserting anywhere else
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
