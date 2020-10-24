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
    
    def recurseTree(self, node, remainingSum, pathNodes, pathsList):
        
        if not node:
            return 
        
        # Add the current node to the path's list
        pathNodes.append(node.val)
        
        # Check if the current node is a leaf and also, if it
        # equals our remaining sum. If it does, we add the path to
        # our list of paths
        if remainingSum == node.val and not node.left and not node.right:
            pathsList.append(list(pathNodes))
        else:    
            # Else, we will recurse on the left and the right children
            self.recurseTree(node.left, remainingSum - node.val, pathNodes, pathsList)
            self.recurseTree(node.right, remainingSum - node.val, pathNodes, pathsList)
            
        # We need to pop the node once we are done processing ALL of it's
        # subtrees.
        pathNodes.pop()    
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        pathsList = []
        self.recurseTree(root, sum, [], pathsList)
        return pathsList
