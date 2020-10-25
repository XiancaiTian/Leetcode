# Leetcode 112 iterative
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
    
# Leetcode 112 recursive
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.target_sum = sum
        self.ans = False
        self.pathSum(root, 0)
        return self.ans
    
    def pathSum(self, root, path_sum):
    
        if root is None:
            return
        
        path_sum += root.val
        
        if root.left is None and root.right is None:
            if path_sum == self.target_sum:
                self.ans = True
        else:
            self.pathSum(root.left, path_sum)
            self.pathSum(root.right, path_sum)
        
        path_sum -= root.val
                        

    
# Leetcode 113
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.ans = []
        self.target_sum = sum
        self.dfs(root, [])
        return self.ans
        
    def dfs(self, root, path_sum):
        if root:
            path_sum.append(root.val)

            if not root.left and not root.right:
                if sum(path_sum) == self.target_sum:
                    self.ans.append(list(path_sum))
                

            else:
                self.dfs(root.left, path_sum)
                self.dfs(root.right, path_sum)

            path_sum.pop()
