# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        balance = True # global variable
        depth, balance = self.readtree(root, 0, balance)
        return balance
        
    def readtree(self, root, depth, balance):
        # if already not balance, stop and return immediately
        if not balance:
            return depth, balance
        elif not root:
            return 0, balance
        # eveything got val, plus one
        # add downstream depth
        depth_left, balance = self.readtree(root.left, depth, balance)
        depth_right, balance = self.readtree(root.right, depth, balance)
        if (depth_left - depth_right) > 1 or (depth_left - depth_right) < -1 :
            balance = False
        depth = 1 + max(depth_left, depth_right)
        return depth, balance
