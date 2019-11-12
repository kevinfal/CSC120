"""
    File: genealogy.py
    Author: Kevin Falconett
    Purpose:
"""

class BST:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def insert(self, added):
        added_node = BST(added)
        if self.val == added:
            return None
        else:
            if added < self.val:
                if self.left is None:
                    self.left = added_node
                    return
                else:
                    self.left.insert(added)
            elif added > self.val:
                if self.right is None:
                    self.right = added_node
                    return
                else:
                    self.right.insert(added)
            else:
                return
    def __str__(self):
        val = str(self.val)
        left = str(self.left.val) if self.left is not None else None
        right = str(self.right.val) if self.right is not None else None

        return "Val: {} Left: {} Right: {}".format(val,self,right)

class Person:
    def __init__(self,name):
        self.name = name




def build_family_tree(rels):
    """
        Parameters:
            rels List(Tuple): list of parent-child relationships
                              list contains tuples of (parent,child)
        Returns:
            Tuple(lookup_tree, family_tree): 
                - lookup_tree is pointer to root of the searcch tree used to
                  map names to family tree nodes
                - family_tree is a pointer to the root of the family tree corresponding
                  to the relationships given 
    """
    pass
    

        

def get_relationship(family_tree,name1,name2):
    """
        Parameters:
            family_tree (Tree): built using build_family_tree()
            name1 (str): name of first person
            name2 (str): name of second person

        Returns:
            Tuple(path1, path2):
                path1 - List(str) of path from lowest common ancestor to 
                        the node with name1
                path2 - List(str) of path from lowest common ancestor to
                        the node with name 2
    """
    pass

def main():
    x = BST(5)
    x.insert(2)
    x.insert(1)
    print(x)
    print(x.left)


if __name__ == "__main__":
    
    main()
