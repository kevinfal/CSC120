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
        added = ListNode(friend)
        if self._friends is None:
            self._friends = added
        else:
            find_tail(self._friends).next = added


    # Override
    def __str__(self):
        return "Name: " +self._name

def make_people_friends(name1,name2):
    """
    Takes two strings and
    :param name1: (str) name of first person
    :param name2: (str) name of second person
    :return: (tuple) containging (Person(name1),Person(name2))
             with their friends set as each other
    """
    p1 = Person(name1)
    p2 = Person(name2)

    p1.add_friend(p2)
    p2.add_friend(p1)

    return (p1,p2)


def construct_relationships(filename):
    people = None
    file = open(filename)
    for line in file:


        line = line.split(' ')
        name1 = line[0]
        name2 = line[1]

        p1 = None
        p2 = None

        p1_in = False
        p2_in = False
        if person_in_linked(people, name1) and person_in_linked(people, name2):
            p1 = find_person(name1)
            p2 = find_person(name2)

            p1.add_friend(name2)
            p2.add_friend(name1)

            p1_in = True
            p2_in = True
        elif person_in_linked(people, name1) and not person_in_linked(people, name2):
            p1 = find_person(people,name1)
            p2 = Person(name2)

            p1.add_friend(name2)
            p2.add_friend(name1)

            p1_in = True
        elif person_in_linked(people, name2) and not person_in_linked(people,name1):
            p2 = find_person(people,name2)
            p1 = Person(name1)

            p1.add_friend(name2)
            p2.add_friend(name1)

            p2_in = True
        else:  # both don't exist

            # convert names into People objects
            p1,p2 = make_people_friends(name1, name2)


        p1_node = ListNode(p1)
        p2_node = ListNode(p2)
        
        if people is None:
            people = p1_node
            people.next = p2_node
        else:
            if p1_in and p2_in:
                continue
            elif p1_in and not p2_in:
                tail = find_tail(people)
                tail.next = p2_node
            elif p2_in and not p1_in:
                tail = find_tail(people)
                tail.next = p1_node
            else:
                tail = find_tail(people)
                tail.next = p1
                tail.next.next = p2

    return people

def find_tail(head):
    if head is None:
        return head
    elif head.next is None:
        return head
    else:
        return find_tail(head.next)


def find_mutual_friends(friend_rels, name1,name2):
    pass


def node_in_linked(head,node):
    if head is None:
        return False
    elif head.val == node.val:
        return True
    else:
        return node_in_linked(head.next,node)


def person_in_linked(head: ListNode,name):
    """

    :param head: (ListNode) that contains a person object
    :param node: (str) representing a person's name
    :return:
    """
    if head is None:
        return False
    elif head.val.get_name() == name:
        return True
    return person_in_linked(head.next,name)


def find_person(head,name):
    if head is None:
        return None
    elif head.val.get_name() == name:
        return head.val
    else:
        return find_person(head.next,name)

def main():
    t = construct_relationships("in02")
    print(t.val.get_friends())


if __name__ == '__main__':
    main()