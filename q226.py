# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """        
        if not root:
            return
        ans = TreeNode(root.val)
        ans.left = self.invertTree(root.right)
        ans.right = self.invertTree(root.left)
        return ans
