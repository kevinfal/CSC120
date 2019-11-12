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
        """
            Searches through the tree
            returns the node with the value of
            target, returns none if not in tree
        """
        # works
        current = self
        stack = [current]

        while len(stack) > 0:
            searched = stack.pop()
            if searched._val == target:
                return searched
            if searched._left is not None:
                stack.append(searched._left)
            if searched._right is not None:
                stack.append(searched._right)
        return None
                

    def bst_search_loop(self, target):
        """
            Searches through the bst
            returns the node with the value of
            target, returns none if not in tree
        """
        # works
        curr = self

        while curr is not None:
            if target < curr._val:
                curr = curr._left
            elif target > curr._val:
                curr = curr._right
            else:
                # target is found
                return curr
        return None

    def bst_insert_loop(self, val):
        """
            Inserts into the bst iteratively
        """
        curr = self
        prev = None
        added = TreeNode(val)

        while curr is not None:
            prev = curr
            if curr._val == val:
                return
            if val < curr._val:
                curr = curr._left
            else:
                curr = curr._right
            
        # here prev is at right spot

        #find where to add to prev
        if val < prev._val:
            prev._left = added
        else:
            prev._right = added
        return self

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

