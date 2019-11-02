#! /usr/bin/python3


from tree_node import *

# we use the same good_vals and bad_vals as the search_1 testcase.  They are
# not even sorted!
from tester_TreeNode_search_1 import get_good_vals, get_bad_vals



def get_bst():
    """Returns a BST, where the values are taken from good_vals(), inserted
in the order they are found in that list.

While the shape and contents of the tree are the same every time, the actual
tree is rebuilt from new objects every time that the function is called."""

    good_vals = get_good_vals()

    tree = TreeNode(good_vals[0])
    for val in good_vals[1:]:
        tree.bst_insert_loop(val)

    return tree



def main():
    print("BEGINNING ANOTHER TEST...")

    tree = get_bst()

    print("The root of the tree is: {}".format(tree.get_val()))

    nodes = [tree]
    next  = 0
    while next < len(nodes):
       this_node = nodes[next]
       next = next+1

       print("Examining the node {}, looking for children...".format(this_node.get_val()))

       left  = this_node.get_left()
       right = this_node.get_right()

       if left is not None:
           print("   Left child: {}".format(left.get_val()))
           nodes.append(left)
       if right is not None:
           print("   Right child: {}".format(right.get_val()))
           nodes.append(right)

    print("TEST COMPLETED")



if __name__ == "__main__":
    main()


