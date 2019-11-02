#! /usr/bin/python3


from tree_funcs import *

# we use the same tree and values as the bst_insert testcase.
from tester_funcs_bst_insert_1 import get_good_vals, get_bad_vals, get_bst

import random
random.seed(0xdead_beef)



def main():
    print("BEGINNING ANOTHER TEST...")

    print("*** NOTE: This testcase will not work properly if your bst_insert_loop() function is not working yet.  So if you failed those testcases, then fix those ones first, then come back and test this one later.")


    good_vals = get_good_vals()
    bad_vals  = get_bad_vals()
    tree      = get_bst()

    # this loop is pretty much the same as the (non-BST) search tester.  Go see
    # that code and comments.

    for x in range(len(good_vals)):
        choice = random.randint(0, len(good_vals)+len(bad_vals))

        if choice < len(good_vals):
            val = good_vals[choice]
            print("Searching for the value {}, which should succeed.".format(val))
        else:
            val = bad_vals[choice - len(good_vals)]
            print("Searching for the value {}, which should fail.".format(val))

        result = bst_search(tree, val)
        if result is None:
            print("    bst_search() returned None.")
        else:
            print("    bst_search() returned a node, with the value {}.".format(result.get_val()))


    print("TEST COMPLETED")



if __name__ == "__main__":
    main()


