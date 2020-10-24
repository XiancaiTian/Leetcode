# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root, 0)
        return self.ans

    def dfs(self, root, sum_of_path):
        if root is None:
            return 0

        sum_of_path = 10*sum_of_path + root.val
        
        # reach leaf node
        if root.left is None and root.right is None:
            self.ans += sum_of_path

        else:
            self.dfs(root.left, sum_of_path)
            self.dfs(root.right, sum_of_path)
            
        sum_of_path = (sum_of_path - root.val) // 10
                
