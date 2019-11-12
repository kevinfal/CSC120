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


    def search(self, target):
        
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
        target = Person(name)
        if self.val == target:
            return target.name
        else:
            returned = self.val.name
            returned = returned + 
    
    def __str__(self):
        val = str(self.val)
        left = str(self.left.val) if self.left is not None else None
        right = str(self.right.val) if self.right is not None else None

        return "Val: {} Left: {} Right: {}".format(val,left,right)

class Person:
    def __init__(self,name):
        self.name = name
        self.parent = None
        self.rel = []
    def add_rel_name(self,name:str):
        added = Person(name)
        self.rel.append(added)
        added.parent = self
    def add_rel_person(self, added):
        self.rel.append(added)
        added.parent = self


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
    fam = lookup.val

    while fam.parent is not None:
        fam = fam.parent
    
    return lookup,fam

        
        

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
    pass

def main():
    rels = [ ("Susana_Shakespeare", "Elizabeth_Hall"),  ("William_Shakespeare", "Hamnet_Shakespeare"),
            ("William_Shakespeare", "Judith_Shakespeare"),  ("William_Shakespeare", "Susana_Shakespeare") ]

    rels2 = [("A","B"),("B","C")]
    tree,fam = build_family_tree(rels2)

    print(fam)
    for x in fam.rel:
        print(x)
        for y in x.rel:
            print(y)

    
        


if __name__ == "__main__":
    
    main()
