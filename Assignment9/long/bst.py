"""
    File: bst.py
    Author: Kevin Falconett
    Purpose: provides class TreeNode, mktree()
             insert(), lca(), find_diff(), and path()

"""

class TreeNode:
    def __init__(self,val):
        self._val = val
        self._left = None
        self._right = None

    # getters
    def get_val(self):
        return self._val
    def get_left(self):
        return self._left
    def get_right(self):
        return self._right
    #setters
    def set_val(self, val):
        self._val = val
    def set_left(self, left):
        self._left = left
    def set_right(self, right):
        self._right = right

    def insert(self, n):
        """
        Inserts an element n into the
        binary tree recursively
        :param n: element to be added
        :return: void
        """
        added = TreeNode(n)  # n made into a node
        val = self.get_val()

        if val == n:
            # n is already in tree
            return None
        
        if val > n:
            # going left (less than)
            if self.get_left() is None:
                # node's left is empty
                # set it as the node's left
                self.set_left(added)
            else:
                #recurse into left
                self.get_left().insert(n)
        elif val < n:
            # going right (greater than)
            if self.get_right() is None:
                # node's right is empty
                # set as the node's right
                self.set_right(added)
            else:
                #recurse into right
                self.get_right().insert(n)

        return

    def path(self, target):
        """
        Finds path from node's root to the node
        with the same value as target. Will return
        None if not found
        :param target: Value of node to find
        :return: List() of all of the elements in
                 the nodes that were traveled through
                 to get to target

                 None if not found/doesnt exist
        """
        val = self.get_val()
        left = self.get_left()
        right = self.get_right()

        if val == target:
            # target is found
            return [target]
        elif self.get_left() is None and self.get_right() is None:
            # if at a leaf node and not found, meaning the node
            # doesn't exist
            return None
        else:
            added = [val]
            if target < val:
                # going left
                if left is None or left.path(target) is None:
                    # impossible to go left (because none)
                    return None
                else:
                    # recurse left
                    added.extend(left.path(target))
            elif val < target:
                # going right
                if right is None or right.path(target) is None:
                    # impossible to go right (None)
                    return None
                else:
                    # recurse right
                    extended = right.path(target)
                    added.extend(extended)
            return added
            
    def __str__(self):
        """
        Tostring for testing
        :return: node in simple string form (value)
        """
        return str(self._val)
        

def mktree(node_list):
    """
    Constructs a binary search tree from the
    values given in a list (in order)
    :param node_list: list elements to be made into nodes
    :return: TreeNode() containing all of the elements found in
             node_list

             (None) if node_list is None or list is empty
    """
    if node_list is None or node_list == []:
        return None

    returned = TreeNode(node_list[0])
    for value in node_list:
        returned.insert(value)
    return returned

def insert(tree, val):
    """
    Inserts TreeNode(val) into tree and
    returns the root
    :param tree: (TreeNode) Root to add val to
    :param val: value to be added to tree
    :return: TreeNode() - tree, the root node we inserted to

             TreeNode(val) if tree is None

    """
    if tree is None:
        return TreeNode(val)
    else:
        tree.insert(val)  # note: val is made into TreeNode(val) here
        return tree

def path(tree, val):
    """
    Constructs the path from the root of tree to a
    node with the value of val
    :param tree: (TreeNode) Root to traverse through
    :param val: Value to path to
    :return: List() path from node's root to the node
            with the same value as target.

            None if not found
            None if either parameter is None
    """
    if tree is None or val is None:
        return None
    else:
        return tree.path(val)

def lca(tree,val1,val2):
    """
    Finds the least common ancestor of nodes with
    the values of val1 and val2
    :param tree: TreeNode() root of tree
    :param val1: first value
    :param val2: second value
    :return: The value of the node that is the least common
             ancestor of the nodes with the values of val1 and val2

            None if Tree, val1, or val2 are None
    """
    if tree is None or val1 is None or val2 is None:
        return None

    path1 = tree.path(val1)
    path2 = tree.path(val2)

    return(find_diff(path1,path2))

def find_diff(l1,l2):
    """
    finds the last shared element in two lists
    recursively
    :param l1: First list
    :param l2: Second List
    :return: The last element of a list that both
             lists share

             i.e find_diff([1,2],[1,3]) returns 1

             None if either list is None
             None if both lists have zero shared elements
    """
    if l1 is None or l2 is None:
        return None
    if l1 == [] or l2 == []:
        return None
    elif l1[0] != l2[0]:
        return None
    if find_diff(l1[1:],l2[1:]) is None:
        return l1[0]
    else:
        returned = [l1[0]]
        returned.append(find_diff(l1[1:],l2[1:]))
        return returned[-1]
