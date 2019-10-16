"""
    File: friends.py
    Author: Kevin Falconett
    Purpose: Provides the class Person, the
             functions construct_relationships(),
             find_mutual_friends(), and several helper
             functions
"""
from list_node import *


class Person:
    """
    Class representing a person
    Fields:
        _name: (str) name
        _friends: (ListNode) list of friends (str)
    """
    def __init__(self, name):
        """
        Initializes person object
        :param name: (str) name of person
        """
        self._name = name
        self._friends = None

    # getters
    def get_name(self):
        """
        getter for person's name
        :return: (str) name
        """
        return self._name

    def get_friends(self):
        """
        getter for person's friends
        :return: (ListNode) linked list of friends
                 will return none if list is empty
        """
        return self._friends

    # setters
    def set_name(self, name):
        """
        sets the person's name
        :param name: (str) name to set
        :return: void
        """
        self._name = name

    def set_friends(self, friends):
        """
        sets the person's list of friends
        :param friends: (ListNode) Linked list of strings
        :return: void
        """
        self._friends = friends

    #  utility
    def add_friend(self, friend):
        """
        Adds friend to this person's list of friends
        :param friend:
        :return: void
        """
        if find_person(self._friends,friend) is None:
            add_node(self._friends,ListNode(friend))

    # Override
    def __str__(self):
        """
        str implementation
        :return: (str) representation of Person
        """
        return "Name: " +self._name

def find_mutual_friends(friend_rels, name1: str,name2: str):
    """
    Finds the friends that both the person with name1 and
    the person with name2 share
    :param friend_rels: (ListNode) Linked list of People objects
    :param name1: Name of first Person
    :param name2: Name of second Person
    :return: (ListNode) Linked list of all friends shared by name1 and name2
    """

    # find person object from friend_rels
    p1 = find_person(friend_rels, name1)
    p2 = find_person(friend_rels, name2)

    if p1 is None or p2 is None:
        return None

    # Gets the linked list of friends of p1 and p2
    friends1 = p1.get_friends()
    friends2 = p2.get_friends()

    return linked_intersect(friends1,friends2)


def construct_relationships(filename):
    """
    Constructs a linked list of people objects with
    all of the friends set in accordance to the inputted
    file
    :param filename: (str) name of file
    :return: Linked list of people in accordance to the text file,
             with the correct friends set for each person object
    """
    people = None
    people_dict = make_people_dict(filename)

    # constructs the linked linst of People
    for name in people_dict:
        added = Person(name)
        added.set_friends(people_dict[name])
        added_node = ListNode(added)
        people = add_node(people,added_node)
    
    return people

def find_person(head: ListNode, name:str):
    """
    Searches a linked list of People and finds the
    person with the matching name
    :param head: (ListNode) linked list to search through
    :param name: (str) name of person
    :return: (Person) with matching name, or
             None if not in list
    """
    if head is None:
        return head
    elif head.val.get_name() == name:
        return head.val
    else:
        return find_person(head.next,name)

def value_in_linked(head, value):
    """
    Searches head for a node who's value matches value,
    determines whether a node with that value is in the
    linked list
    :param head: (ListNode) Linked List to iterate through
    :param value: value to look for
    :return: True if there is a node with matching value
             False otherwise
    """
    if head is None:
        return head
    elif head.val == value:
        return head.val
    else:
        return find_person(head.next,value)


def linked_intersect(head1,head2):
    """
    Finds all elements present in both head1 and head2
    :param head1: (ListNode) first linked list
    :param head2: (ListNode) second linked list
    :return: (ListNode) Linked List containing all shared
             nodes between head1 and head2
    """
    returned = None
    curr = head1
    while curr is not None:
        if value_in_linked(head2,curr):
            returned = add_node(returned,curr)
        curr = curr.next
    
    return returned

def make_people_dict(filename):
    """
    Iterates through a text file and constructs a
    dictionary with names as keys and a Linked List containing
    their friends as values
    :param filename: (str) name of text file
    :return: Dict(str:ListNode(str)) - a Dictionary with names as keys
             and a linked list with friends as values
    """
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


def find_tail(head):
    """
    Gets the last node of a Linked List
    :param head: (ListNode) linked list to traverse
    :return: (ListNode) Last node of a Linked List
    """
    if head is None:
        return head
    elif head.next is None:
        return head
    else:
        return find_tail(head.next)

def add_node(head: ListNode, added: ListNode):
    """
    Adds a node to the end of a linked list
    :param head: (ListNode) Linked list to add to
    :param added: (ListNode) Node to add to list
    :return: (ListNode) with all Nodes in head with added at
             the end
    Precondition:
        Added.next must be none, or else may not function properly
    """
    if head is None:
        return added
    else:
        tail = find_tail(head)
        tail.next = added
        return head
