# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
                
        lst = []
        self.recursion(root, lst)
        self.lst = lst
        self.length = len(lst)
        self.index = 0
        
    def recursion(self, root, lst):
        if root:
            self.recursion(root.left, lst)
            lst.append(root.val)
            self.recursion(root.right, lst)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        ans = self.lst[self.index]
        self.index+=1
        return ans
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index< self.length


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
