class TreeNode:
    def __init__(self,val):
        self._val = val
        self._left = None
        self._right = None

    # getters
    def get_val(self):
        return self._val
    def get_left(self):
        return self._left
    def get_right(self):
        return self._right
    #setters
    def set_left(self, left):
        self._left = left
    def set_right(self, right):
        self._right = right

    def search(self,target):
        left = self._left
        right = self._right
        val = self._val
        if target == val:
            return self
        else:

            if left is not None:
                self.search(left)
            if right is not None:
                self.search(right)
            
            if val != val:
                return None
            
    def bst_search_loop(self,val):
        
        current = self

        if current._val == val:
            return current
        while current is not None and current._val != val:
            if current._val < val:
                current = current._left
            elif current._val > val:
                current = current._right
        
        return current

    def bst_insert_loop(self,val):
        
        current = self
        added = TreeNode(val)
        
        while current is not None:
            # already added
            if current._val == val:
                return None
            # target less than val
            if current._val > val:
                prev = current
                current = current._left
                if current is None:
                    prev._left = added
                    return 
            # target greater than val
            elif current._val < val:
                prev = current
                current = current._right
                if current is None:
                    if prev._right is None:
                        prev._right = added
                        return


    def __str__(self):
        """
        Tostring for testing
        :return: node in simple string form (value)
        """

        val = str(self._val)
        left = ''
        right = ''
        if self._left is None:
            left = None
        else:
            left = str(self._left._val)
        if self._right is None:
            right = None
        else:
            right = str(self._right._val)
        

        return "val: {}, left: {}, right: {}".format(val,left,right)
        
def main():
    x = TreeNode(5)
    x.bst_insert_loop(1)
    x.bst_insert_loop(10)
    x.bst_insert_loop(2)
    x.bst_insert_loop(3)
    print(x)
    print(x._left._right)


if __name__ == "__main__":
    
    main()
