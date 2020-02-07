# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        lst = []
        self.k = k-1
        self.recursion(root, lst)
        return lst[self.k]
    
    
    def recursion(self, root, lst):
        # try to skip the rest of the recursion
        if len(lst)> self.k:
            return 
        if root:
            self.recursion(root.left, lst)
            lst.append(root.val)
            self.recursion(root.right, lst)
