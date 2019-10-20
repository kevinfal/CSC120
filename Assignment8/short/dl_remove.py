"""
    File: dl_remove.py
    Author: Kevin Falconett
    Purpose: provides dl_remove() which removes a node from a linked list
"""

def dl_remove(head, node_to_remove):
    """
    removes node from linked list
    :param head: linked list
    :param node_to_remove: node to be removed
    :return: linked list after change
    """

    curr = head
    
    while curr is not None:
        if curr.get_val() == node_to_remove.get_val():
            
            if curr.get_prev() is None:
                head = curr.get_next()
                head.set_prev(None)
            elif curr.get_next() is None:
                curr.get_prev().set_next(None)
                
            else:
                prev = curr.get_prev()
                next= curr.get_next()
                prev.set_next(next)
                next.set_prev(prev)
            return head
        curr = curr.get_next()
    return head
