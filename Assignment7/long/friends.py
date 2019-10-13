"""
    File: friends.py
    Author: Kevin Falconett

"""
from list_node import *


def value_in_linked(head, val):
    curr = head
    while curr is not None:
        if curr == val:
            return True
        curr = curr.next
    return False


def insert(head, added):
    E = head
    if head is None:
        return added
    elif E is None or E.val < added.val:
        # E is empty or added greater than E
        # makes added the new front of E
        added.next = head
        E = added
    else:
        curr = E
        while curr is not None:
            # Element is greater than curr
            # and its next is less than curr
            # and inserts
            if curr.val > added.val and (curr.next == None
                                         or curr.next.val < added.val):
                next = curr.next
                curr.next = added
                added.next = next
            curr = curr.next
    return E


class Person:
    def __init__(self, name):
        self._name = name
        self._friends = None

    # getters
    def get_name(self):
        return self._name

    def get_friends(self):
        return self._friends

    # setters
    def set_name(self, name):
        self._name = name

    def set_friends(self, friends):
        self._friends = friends

    #  utility
    def add_friend(self, friend):
        if self._friends is None:
            self._friends = friend
        elif not value_in_linked(friend):
            insert(self._friends, friend)

    # Override
    def __str__(self) -> str:
        return "Name: {}, Friends: {}".format(self._name, self._friends)



