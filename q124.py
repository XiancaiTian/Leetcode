# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """    
        maxi = root.val
        self.max = None # the true answer
        summ = self.readtree(root)
        return self.max
    
    def readtree(self, root):
        if not root:
            return 0
        # eveything got val, plus one
        # add downstream depth
        summ_left = self.readtree(root.left)
        summ_right = self.readtree(root.right)
        
        # this question is ask about path, not sum of triangle
        if root.val:
            summ_left = max(0, summ_left)
            summ_right = max(0, summ_right)
        temp = root.val + summ_left + summ_right
        self.max = max(temp, self.max)
        summ = root.val + max(summ_left, summ_right)
        return summ
