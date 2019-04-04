# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        self.readtree(root, 0)
        return self.ans
    
    def readtree(self, root, loc):
        if not root:
            return
        if loc <= len(self.ans)-1:
            self.ans[loc] = root.val
        else:
            self.ans.insert(loc,root.val)
        self.readtree(root.left, loc+1)
        self.readtree(root.right, loc+1)
