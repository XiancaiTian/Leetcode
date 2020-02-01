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
        stack = [(root, 0)]
        maxdepth = 0
        
        while stack:
            root, depth = stack.pop()
            if root:
                depth += 1
                maxdepth = max(maxdepth, depth)
                stack.append((root.right, depth))
                stack.append((root.left, depth))
            
        return maxdepth
