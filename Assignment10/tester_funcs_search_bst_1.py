#! /usr/bin/python3


from tree_node  import *
from tree_funcs import *

# we use the same values and tree as the bst_insert_loop_1 testcase.
from tester_TreeNode_bst_insert_loop_1 import get_good_vals, get_bad_vals, get_bst

import random
random.seed(0xdead_beef)



def main():
    """Core of this testcase.  Uses our input dataset; iterates through all
nodes, and tests count() and is_bst() at every node."""


    print("BEGINNING ANOTHER TEST...")

    good_vals = get_good_vals()
    bad_vals  = get_bad_vals()
    tree      = get_bst()


    # breadth-first search through the tree.  Do search() at every point,
    # seaching for 2 good values, and 1 bad value, from every location.

    nodes = [tree]
    next  = 0
    while next < len(nodes):
       this_node = nodes[next]
       next = next+1

       g1 = random.randint(0, len(good_vals)-1)
       g2 = random.randint(0, len(good_vals)-1)
       b1 = random.randint(0, len( bad_vals)-1)

       good1 = good_vals[g1]
       good2 = good_vals[g2]
       bad1  =  bad_vals[b1]

       print("Examining the node {} :".format(this_node.get_val()))
       print("    The search for the root value {} must certainly work!".format(this_node.get_val()))
       print("    The search for the good values {},{} might work, or might fail, if we are in the wrong subtree.".format(good1,good2))
       print("    The search for the bad value {} will definitely fail.".format(bad1))

       result = search(this_node, this_node.get_val())
       if result is None:
           print("    search({}) returned None".format(this_node.get_val()))
       else:
           print("    search({}) returned a node with value {}".format(this_node.get_val(), result.get_val()))

       result = search(this_node, good1)
       if result is None:
           print("    search({}) returned None".format(good1))
       else:
           print("    search({}) returned a node with value {}".format(good1, result.get_val()))

       result = search(this_node, good2)
       if result is None:
           print("    search({}) returned None".format(good2))
       else:
           print("    search({}) returned a node with value {}".format(good2, result.get_val()))

       result = search(this_node, bad1)
       if result is None:
           print("    search({}) returned None".format(bad1))
       else:
           print("    search({}) returned a node with value {}".format(bad1, result.get_val()))



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


