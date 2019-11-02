#! /usr/bin/python3


from tree_node import *

import random

# we use the random number generator to generate long strings of integers,
# since that's easier than building the lists by hand.  But, we want them
# to be predictable, run to run.  So we "seed" the RNG (random number
# generator), so that every run of this testcase will generate the same
# sequence.
#
# To build a new dataset, we can simply change the seed.

random.seed(0xdead_beef)



#------------------
# We have functions to generate the good_vals, bad_vals, and tree.
# We could, of course, place all of this in main(), but if we place
# it into these functions, then it will be possible to use these
# files, through imports, as easy input datasets for other testcases.
#
# We'll declare three functions:
#    get_good_vals()     - things which are in the tree
#    get_bad_vals()      - things which are *NOT* in the tree
#    get_unsorted_tree() - a non-BST tree
#------------------

def get_good_vals():
    """Return a list of values, which will be inserted into this dataset's
tree.  The values are not sorted, but we guarantee that the list has no
duplicates.

This function is guaranteed to return the same set of values every time it
is called, even if called multiple times in one process."""

    return [41, -45, -31, 20, 24, 44, 60, 50, 18, 99, -1, 57, -30, 27, 64, 65]



def get_bad_vals():
    """Return a list of values, which contains no duplicates and which also
has no values in common with the good_vals() above.

This list is randomly generated, and so if you call the function twice in the
same program, you will get different lists."""

    good_vals = get_good_vals()

    retval = []
    while len(retval) < len(good_vals)//2:
        new_val = random.randint(-50,100)
        if new_val in good_vals or new_val in retval:
            continue    # duplicate, try again
        retval.append(new_val)
    return retval



def get_tree():
    """Return a tree - this is *NOT* assumed to be a BST!

While the actual nodes of the tree are generated in this function - and thus,
different calls will result in different trees - the shape and contents of the
tree will be the same, each time it is called."""

    # this function tests the TreeNode.search() function; we don't want to
    # test the insert() function yet.  So I've generated a tree by hand,
    # and I'll build it with the getters here.

    good_vals = get_good_vals()
    assert len(good_vals) == 16

    a = TreeNode(good_vals[ 0])
    b = TreeNode(good_vals[ 1])
    c = TreeNode(good_vals[ 2])
    d = TreeNode(good_vals[ 3])
    e = TreeNode(good_vals[ 4])
    f = TreeNode(good_vals[ 5])
    g = TreeNode(good_vals[ 6])
    h = TreeNode(good_vals[ 7])
    i = TreeNode(good_vals[ 8])
    j = TreeNode(good_vals[ 9])
    k = TreeNode(good_vals[10])
    l = TreeNode(good_vals[11])
    m = TreeNode(good_vals[12])
    n = TreeNode(good_vals[13])
    o = TreeNode(good_vals[14])
    p = TreeNode(good_vals[15])

    a.set_left (b)
    a.set_right(c)

    # b is a leaf

    c.set_left (d)
    c.set_right(e)

    # d only has a right child
    d.set_right(f)

    # e only has a left child
    e.set_left (g)

    # f is a leaf

    g.set_left (h)
    g.set_right(i)

    # h is a leaf

    i.set_left (j)
    i.set_right(k)

    j.set_left (l)
    j.set_right(m)

    # k only has a right child
    k.set_right(n)

    l.set_left (o)
    l.set_right(p)

    # m,n,o,p are all leaves

    return a



def main():
    """Core of this testcase.  Uses our input dataset; randomly chooses what
values to search for, using the RNG to decide."""


    print("BEGINNING ANOTHER TEST...")

    good_vals = get_good_vals()
    bad_vals  = get_bad_vals()
    tree      = get_tree()


    # we'll do a bunch of tests, in random order.  Some will be expected to be
    # hits, and other misses.

    for x in range(len(good_vals)):
        choice = random.randint(0, len(good_vals)+len(bad_vals))

        if choice < len(good_vals):
            val = good_vals[choice]
            print("Searching for the value {}, which should succeed.".format(val))
        else:
            val = bad_vals[choice - len(good_vals)]
            print("Searching for the value {}, which should fail.".format(val))

        result = tree.search(val)
        if result is None:
            print("    tree.search() returned None.")
        else:
            print("    tree.search() returned a node, with the value {}.".format(result.get_val()))


    print("TEST COMPLETED")



if __name__ == "__main__":
    main()


