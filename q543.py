# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.length = 0
        self.dfs_visit_every_node(root)
        return self.length
        
    def dfs_visit_every_node(self, root):
        if root:
            depth_left = self.dfs_visit_every_node(root.left)
            depth_right = self.dfs_visit_every_node(root.right)
            self.length = max(self.length, depth_left + depth_right)
            return max(depth_left, depth_right) + 1
        else:
            return 0
