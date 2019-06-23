# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        self.helper(root, stack)
        return stack
    
    # recursive soln
    def helper(self, root, stack):
        if root:
            if root.left:
                self.helper(root.left, stack)
            if root.right:
                self.helper(root.right, stack)
            stack.append(root.val)
        return stack
