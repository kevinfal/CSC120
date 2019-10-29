

class TreeNode:
    def __init__(self,val):
        self._val = val
        self._left = None
        self._right = None

    
    def get_val(self):
        return self._val
    def get_left(self):
        return self._left
    def get_right(self):
        return self._right
    
    def set_val(self, val):
        self._val = val
    def set_left(self, left):
        self._left = left
    def set_right(self, right):
        self._right = right

    def insert(self, n):
        added = TreeNode(n)
        val = self.get_val()
        if val == n:
            return None
        
        if val > n:
            if self.get_left() is None:
                self.set_left(added)
            else:
                self.get_left().insert(n)
        elif val < n:
            if self.get_right() is None:
                self.set_right(added)
            else:
                self.get_right().insert(n)
        return

    def path(self, target):
        val = self.get_val()
        left = self.get_left()
        right = self.get_right()

        if val == target:
            return [target]
        elif self.get_left() is None and self.get_right() is None:
            return None
        else:
            added = [val]
            if target < val:
                if left is None or left.path(target) is None:
                    return None
                else:
                    added.extend(left.path(target))
            elif val < target:
                if right is None or right.path(target) is None:
                    return None
                else:
                    extended = right.path(target)
                    added.extend(extended)
            return added
            
    def __str__(self):
        return str(self._val)
        

def mktree(node_list):
    if node_list is None or node_list == []:
        return None

    returned = TreeNode(node_list[0])
    for value in node_list:
        returned.insert(value)
    return returned

def insert(tree, val):
    if tree is None:
        return TreeNode(val)
    else:
        tree.insert(val)
        return tree

def path(tree, val):
    if tree is None or val is None:
        return None
    else:
        return tree.path(val)

def lca(tree,val1,val2):
    if tree is None or val1 is None or val2 is None:
        return None
    path1 = tree.path(val1)
    path2 = tree.path(val2)
    return(find_diff(path1,path2))

def find_diff(l1,l2):
    if l1 is None or l2 is None:
        return None
    if l1 == [] or l2 == []:
        return None
    elif l1[0] != l2[0]:
        return None
    if find_diff(l1[1:],l2[1:]) is None:
        return l1[0]
    else:
        returned = [l1[0]]
        returned.append(find_diff(l1[1:],l2[1:]))
        return returned[-1]
        



def main():
    x = mktree([6,8,3,1,4,2,9])
    path1 = x.path(2)
    path2 = x.path(4)
    print(find_diff(path1,path2))
    
        
if __name__ == "__main__":
    main()