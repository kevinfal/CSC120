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
        """
            Standard BST recursive insert for any
            data type that supports comparisons

            Parameters:
                added: Can be any type that supports comparisons

            Returns:
                void (None)
        """
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


    def search(self, target):
        """
            Recursively searches through bst for a node with
            a value that == target, returns none
            if not found

            Parameters:
                target: any object that supports comparisons

            Returns:
                Node (BST) that contains a value == target
        """
        if self.val == target:
            return self
        else:
            if target < self.val:
                
                if self.left is None:
                    return None
                else:
                    return self.left.search(target)
            elif target > self.val:
                if self.right is None:
                    return None
                else:
                    return self.right.search(target)
            else:
                return None
    

    def path_strings(self, name):
        """
            Finds the path from the root of a BST to
            a node ethat has a Person object with the same
            name as name in the form of a List of strings
            containing the nodes passed along the way

            Parameters:
                name (str): name of Person to find
            
            Returns:
                List(str) of every Person object passed on
                the way to the target person object + the
                target person
        """
        target = Person(name)

        # if found
        if self.val == target:
            return [name]
        else:
            returned = [self.val.name]  # list of visted nodes

            #standard binary search operations

            if target < self.val:
                # target is less than, recurse left
                if self.left is None:
                    # should be there but doesn't exist
                    return []
                else:
                    # add node to returned
                    returned.extend(self.left.path_strings(name))

            elif target > self.val:
                # target greater than, recurse right
                if self.right is None:
                    # should be there but doesn't exist
                    return []
                else:
                    returned.extend(self.right.path_strings(name))


            return returned
    
    
    def __str__(self):
        """
            Str override
        """
        val = str(self.val)
        left = str(self.left.val) if self.left is not None else None
        right = str(self.right.val) if self.right is not None else None

        return "Val: {} Left: {} Right: {}".format(val,left,right)

class Person:
    def __init__(self,name):
        self.name = name
        self.parent = None
        self.rel = []

    def add_rel_person(self, added: Person):
        """
            adds a Person object to this Objects rel[],
            adds relationship from this object to another

            Updates the added Person's parent field to this object

            Parameters:
                added (Person): person to add to self.rel
        """
        self.rel.append(added)
        added.parent = self

    # Overrides
    def __eq__(self, other):
        return self.name == other.name
    def __lt__(self, other):
        return self.name < other.name
    def __le__(self, other):
        return self.name <= other.name
    def __gt__(self,other):
        return self.name > other.name
    def __ge__(self,other):
        return self.name >= other.name
    def __str__(self):
        return "Name: {}".format(self.name)



def build_family_tree(rels: list):
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
    lookup = create_lookup(rels)
    lookup = update_relationships(lookup,rels)
    fam = find_root(lookup)

    return lookup,fam

def find_root(lookup):
    returned = lookup.val
    while returned.parent is not None:
        returned = returned.parent
    return returned
        

def update_relationships(lookup,rels):
    for relation in rels:
        name1 = relation[0]
        name2 = relation[1]
        search_person1 = Person(name1)
        search_person2 = Person(name2)
        
        person1 = lookup.search(search_person1).val
        person2 = lookup.search(search_person2).val
        
        person1.add_rel_person(person2)
    return lookup


def create_lookup(rels):
    lookup = None
    for relation in rels:
        name1 = relation[0]
        name2 = relation[1]
        person1 = Person(name1)
        person2 = Person(name2)
        if not lookup:
            lookup = BST(person1)
            lookup.insert(person2)
        else:
            lookup.insert(person1)
            lookup.insert(person2)
    return lookup

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
    if family_tree is None:
        return None
    lca = find_lca(family_tree,name1,name2)
    path1 = find_path(lca,name1)
    path2 = find_path(lca,name2)
    return (path1,path2)

def find_lca(tree,name1,name2):
    target = find_lca_name(tree,name1,name2)
    return find_person(tree,target)

def find_lca_name(tree,name1, name2):
    path1 = find_path(tree,name1)
    path2 = find_path(tree, name2)

    lca_index = 0
    for i in range(len(path1)):
        if i > len(path2) -1:
            lca_index = i - 1
            break
        if path1[i] != path2[i]:
            lca_index = i - 1
            
    
    lca_name = path1[lca_index]

    return lca_name
        
def find_person(tree: Person, name):
    target = Person(name)
    if tree == target:
        return tree
    else:
        paths = tree.rel
        for path in paths:
            returned = find_person(path,name)
            if returned == target:
                return returned
        return tree



def find_path(tree: Person,name):
    target = Person(name)
    if tree == target:
        return [target.name]

    else:
        if tree.rel == []: # dead end
            return None
        returned = [tree.name]
        paths = tree.rel
        path_names = []
        for person in paths:
            path_names.append(person.name)
        for path in paths:
            # only do this if not found yet
            if name not in returned:
                added = find_path(path,name)
                if added is not None:
                    returned.extend(added)
        return returned


def main():
    rels = [ ("Susana_Shakespeare", "Elizabeth_Hall"),  ("William_Shakespeare", "Hamnet_Shakespeare"),
            ("William_Shakespeare", "Judith_Shakespeare"),  ("William_Shakespeare", "Susana_Shakespeare") ]

    rels2 = [('B', 'E'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'F'), ('B', 'G')]
    tree,fam = build_family_tree(rels2)

    res = find_path(fam,'C')
    print(res)
    
        


if __name__ == "__main__":
    
    main()
