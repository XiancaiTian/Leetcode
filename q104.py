# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.readtree(root, 0)
        
    def readtree(self, root, depth):
        if not root:
            return 0
        # eveything got val, plus one
        # add downstream depth
        depth_left = self.readtree(root.left, depth)
        depth_right = self.readtree(root.right, depth)
        depth = 1 + max(depth_left, depth_right)
        return depth
