"""
    File: tree_Funcs.py
    Author: Kevin Falconett
    Purpose: To make me suffer
"""
from tree_node import *

def count(root):
    """
        Counts the amount of elements in a tree
        basically len()
    """
    if root is None:
        return 0
    left = root.get_left()
    right = root.get_right()
    sum = 1

    if left is not None:
        sum = sum + count(left)
    if right is not None:
        sum = sum + count(right)
    
    return sum

def is_bst(root):
    """
        Checks if a tree is a binary
        search tree

        True if binary search tree
        False otherwise
    """
    if root is None or count(root) == 1:
        return True

    tree = pre_order_traversal_nodes(root)
    for node in tree:
        if not checkNode(node):
            return False

    return True
        
def checkNode(node):
    """
        Helper function for is_bst
        checks if the node is valid for
        a bst
    """
    left = node.get_left()
    right = node.get_right()
    val = node.get_val()

    if left is None or left.get_val() < val:
        if right is None or right.get_val() > val:
            return True
    return False



def search(root, target):
    """
        Searches for a node in a tree
        returns that node
    """
    if root is None:
        return None
    current = root
    stack = [current]

    while len(stack) > 0:
        searched = stack.pop()
        if searched._val == target:
            return searched
        if searched._left is not None:
            stack.append(searched._left)
        if searched._right is not None:
            stack.append(searched._right)
    return None

def bst_search(root,target):
    """
        Searches through a binary
        search tree fora node
        with value target
    """
    if root is None:
        return None
    curr = root

    while curr is not None:
        if target < curr._val:
            curr = curr._left
        elif target > curr._val:
            curr = curr._right
        else:
            # target is found
            return curr
    return None


def bst_insert(root, target):
    """
        Insets into a binary search tree
        recursively
    """
    added = TreeNode(target)
    if root is None:
        return added
    val = root.get_val()

    if val == target:
        # target is already in tree
        return None
    if val > target:
        # going left (less than)
        if root.get_left() is None:
            root.set_left(added)
        else:
            #recurse into left
            bst_insert(root.get_left(),target)
    elif val < target:
        # going right (greater than)
        if root.get_right() is None:
            # set as the node's right
            root.set_right(added)
        else:
            #recurse into right
            bst_insert(root.get_right(),target)
    return root
def pre_order_traversal_nodes(root):
    """
        Traverses through a tree via
        Pre-Order traversal recursively
        and returns a list of all the nodes
        in the tree
    """
    if root is None:
        return []
    left = root.get_left()
    right = root.get_right()

    returned = [root]
    returned.extend(pre_order_traversal_nodes(left))
    returned.extend(pre_order_traversal_nodes(right))
    return returned

def pre_order_traversal(root):
    """
        Traverses a tree via pre-order
        recursively. Returns a list of
        all values of the nodes
    """
    if root is None:
        return []
    left = root.get_left()
    right = root.get_right()
    val = root.get_val()
    
    returned = [val]
    returned.extend(pre_order_traversal(left))
    returned.extend(pre_order_traversal(right))

    return returned

def post_order_traversal(root):
    """
        Traverses a tree in
        Post-Order recursively
        returns list of all values
        of the nodes
    """
    if root is None:
        return []
    left = root.get_left()
    right = root.get_right()
    val = root.get_val()
    returned = []
    returned.extend(post_order_traversal(left))
    returned.extend(post_order_traversal(right))

    returned.extend([val])
    return returned

def in_order_traversal(root):
    """
        Traverses a tree in
        In-Order recursively
        returns list of all values
        of the nodes
    """
    if root is None:
        return []
    left = root.get_left()
    right = root.get_right()
    val = root.get_val()

    returned = []
    
    returned.extend(in_order_traversal(left))
    returned.extend([val])
    returned.extend(in_order_traversal(right))
    
    return returned