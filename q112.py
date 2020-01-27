# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        stack = [(root, 0)]
        while stack:
            (root, path) = stack.pop()
            if root:
                path += root.val
                stack.append((root.right, path))
                stack.append((root.left, path))
                if not root.left and not root.right:
                    if path == sum: return True
        return False
