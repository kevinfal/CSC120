#! /usr/bin/python3

from tree_node import *



def main():
    print("BEGINNING THE TEST OF THE BASIC MECHANISMS OF THE TreeNode CLASS")

    required  = {"get_val", "get_left", "get_right", "set_left", "set_right"}
    forbidden = {"set_val", "val", "left", "right"}
    actual = set(dir(TreeNode))

    if actual & required != required:
        print("ERROR: Not all of the required methods of TreeNode were implemented.")
        return

    if actual & forbidden != set():
        print("ERROR: One or more forbidden names were declared in TreeNode.")
        return


    # can we create a few nodes, and do trivial operations?
    a = TreeNode(1)
    b = TreeNode("abc")

    if a.get_val() != 1 or b.get_val() != "abc":
        print("ERROR: get_val() is not returning the proper values.")
        return

    if a.get_left() is not None or a.get_right() is not None or \
       b.get_left() is not None or b.get_right() is not None:
        print("ERROR: In newly-created nodes, get_left() or get_right() are not returning None.")
        return

    a.set_left(b)
    if a.get_left() is not  b   or a.get_right() is not None or \
       b.get_left() is not None or b.get_right() is not None:
        print("ERROR: In a trivial tree, get_left() or get_right() are not returning the proper values.")
        return


    print("TEST COMPLETED")



if __name__ == "__main__":
    main()


