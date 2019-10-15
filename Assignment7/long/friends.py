"""
    File: friends.py
    Author: Kevin Falconett

"""
from list_node import *


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
        if not value_in_linked(self._friends,friend):
            add_node(self._friends,ListNode(friend))
        


    # Override
    def __str__(self):
        return "Name: " +self._name

def find_mutual_friends(friend_rels, name1: str,name2: str):
    p1 = find_person(friend_rels, name1)
    p2 = find_person(friend_rels, name2)

    if p1 is None or p2 is None:
        return None

    friends1 = p1.get_friends()
    friends2 = p2.get_friends()

    return linked_intersect(friends1,friends2)


def construct_relationships(filename):

    people = None
    
    people_dict = make_people_dict(filename)

    for name in people_dict:
        added = Person(name)
        added.set_friends(people_dict[name])
        added_node = ListNode(added)
        people = add_node(people,added_node)
    
    return people

def find_person(head: ListNode, name:str):
    if head is None:
        return head
    elif head.val.get_name() == name:
        return head.val
    else:
        return find_person(head.next,name)


def linked_intersect(head1,head2):
    returned = None

    curr = head1
    while curr is not None:
        if value_in_linked(head2,curr):
            returned = add_node(returned,curr)
        curr = curr.next
    
    return returned

def make_people_dict(filename):
    people_dict = dict()

    file = open(filename)

    for line in file:

        line = line.split()

        name1 = line[0]
        name2 = line[1]

        name1_node = ListNode(name1)
        name2_node = ListNode(name2)

        if name1 in people_dict:
            people_dict[name1] = add_node(people_dict[name1],name2_node)
        else:
            people_dict[name1] = name2_node
        if name2 in people_dict:
            people_dict[name2] = add_node(people_dict[name2],name1_node)
        else:
            people_dict[name2] = name1_node
    
    return people_dict



def value_in_linked(head,value):
    value = ListNode(value)
    if head is None:
        return False
    elif head == value:
        return True
    else:
        return value_in_linked(head.next,value)

def find_tail(head):
    if head is None:
        return head
    elif head.next is None:
        return head
    else:
        return find_tail(head.next)

def add_node(head: ListNode, added: ListNode):
    if head is None:
        return added
    else:
        tail = find_tail(head)
        tail.next = added
        return head



def main():
    t = construct_relationships("in04.txt")
    
    find_mutual_friends(t,"William", "Rebecca")



if __name__ == '__main__':
    main()