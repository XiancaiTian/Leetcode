# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# should consider every node as a new start

# should return the better path in each recursion
# Note: there is no need to reach the leaf

# better path is selected from 
# (self + left, self + right, self only, self + left + right)

# return path is selected from 
# (self + left, self + right, self only)

# edge case, what if the tree looks like [-5]

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxi_sum = root.val
        self.dfs(root)
        return self.maxi_sum

    def dfs(self, root):
        if root:
            left_path = self.dfs(root.left)
            right_path = self.dfs(root.right)
            
            three_options = max(root.val, 
                              root.val + left_path, 
                              root.val + right_path)
            
            self.maxi_sum = max(self.maxi_sum, 
                                three_options, 
                                root.val + left_path + right_path)
            return three_options
        
        else:
            return 0
            

