"""
    File: dlist_node.py
    Author: Kevin Falconett
"""

class DListNode:
    def __init__(self,val):
        self._val = val
        self._next = None
        self._prev = None
    
    def get_val(self):
        return self._val
    def get_next(self):
        return self._next
    def get_prev(self):
        return self._prev
    
    def set_val(self,val):
        self._val = val
    def set_next(self,next):
        self._next = next
    def set_prev(self,prev):
        self._prev = prev
    
    def __str__(self):
        '''
        Purpose: print the values of the list separated by '->' or
        '<->'. The latter only if linked in both directions
        Note: check for circular list taken directly from the earlier
        provided ListNode class
        '''
        string = ''
        objs = []
        cur = self
        while cur is not None:
            cur_val = str(cur._val)
            string += cur_val
            
            if cur._next is None:
                string += '->'
            elif cur._next._prev is not cur:  # if only linked one way
                string += '->'
            else:  # if doubly linked
                string += '<->'  

            if cur in objs:
                string += "{} -> ... (to infinity and beyond)".format(cur_val)
                return string
            else:
                objs.append(cur)
            cur = cur._next

        return string + 'None'

    def __eq__(self,other):
        if isinstance(other,DListNode):
            return self._val == other.get_val
        else:
            return False
