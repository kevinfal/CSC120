#! /usr/bin/python3


from tree_node  import *
from tree_funcs import *

# we use the same values and tree as the bst_insert_loop_1 testcase.
from tester_TreeNode_bst_insert_loop_1 import get_good_vals, get_bad_vals, get_bst



def main():
    """Core of this testcase.  Uses our input dataset; iterates through all
nodes, and tests count() and is_bst() at every node."""


    print("BEGINNING ANOTHER TEST...")

    tree = get_bst()


    # breadth-first search through the tree.  Do count() and is_bst() at
    # every point.

    nodes = [tree]
    next  = 0
    while next < len(nodes):
       this_node = nodes[next]
       next = next+1

       print("Examining the node {} :".format(this_node.get_val()))
       print("    pre order traversal : {}".format(pre_order_traversal(this_node)))
       print("    in order traversal : {}".format(in_order_traversal(this_node)))
       print("    post order traversal : {}".format(post_order_traversal(this_node)))

       left  = this_node.get_left()
       right = this_node.get_right()

       if left is not None:
           print("    Left child: {}".format(left.get_val()))
           nodes.append(left)
       if right is not None:
           print("    Right child: {}".format(right.get_val()))
           nodes.append(right)


    print("TEST COMPLETED")



if __name__ == "__main__":
    main()


