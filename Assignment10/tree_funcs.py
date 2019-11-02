
from tree_node import *

def count(root):
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
    if root is None or count(root) == 1:
        return True

    tree = pre_order_traversal_nodes(root)
    #print(tree)
    for node in tree:
        if not checkNode(node):
            return False

    return True
        
def checkNode(node):
    left = node.get_left()
    right = node.get_right()
    val = node.get_val()

    if left is None or left.get_val() < val:
        if right is None or right.get_val() > val:
            return True
    return False

    

def check_bst_recur(root):
    if root is None:
        return True
    left_val = root.get_left().get_val() if root.get_left() is not None else None
    
    right_val = root.get_right().get_val() if root.get_right() is not None else None
    val = root.get_val()

    if left_val is None or  left_val < val:
        if right_val is None or right_val > val:
            return True
    else:
        return False
    
    if check_bst_recur(root.get_left()) == False or check_bst_recur(root.get_right()) == False:
        return False

    return True


def search(root, target):
    if root is None:
        return None
    left = root.get_left()
    right = root.get_right()
    val = root.get_val()

    if val == target:
        return root
    else:
        if left is not None:
            search(left,target)
        if right is not None:
            search(right,target)
        return None

def bst_search(root,target):
    if root is None:
        return None
    left = root.get_left()
    right = root.get_right()
    val = root.get_val()

    if val == target:
        return root
    else:
        if target < val:
            if left is not None:
                bst_search(left,target)
        else:
            if left is not None:
                bst_search(right,target)
        
        return None

def bst_insert(root, target):
    
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
            # node's left is empty
            # set it as the node's left
            root.set_left(added)
        else:
            #recurse into left
            root.get_left().insert(target)
    elif val < target:
        # going right (greater than)
        if root.get_right() is None:
            # node's right is empty
            # set as the node's right
            root.set_right(added)
        else:
            #recurse into right
            root.get_right().insert(target)

    return
def pre_order_traversal_nodes(root):
    if root is None:
        return []
    left = root.get_left()
    right = root.get_right()

    returned = [root]
    returned.extend(pre_order_traversal_nodes(left))
    returned.extend(pre_order_traversal_nodes(right))
    return returned

def pre_order_traversal(root):
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
    if root is None:
        return []
    left = root.get_left()
    right = root.get_right()
    val = root.get_val()
    returned = []

    post_order_traversal(left)
    post_order_traversal(right)
    returned.extend([val])

    return returned

def in_order_traversal(root):
    if root is None:
        return []
    left = root.get_left()
    right = root.get_right()
    val = root.get_val()

    returned = []
    
    in_order_traversal(left)
    returned.extend([val])
    in_order_traversal(right)
    
    return returned