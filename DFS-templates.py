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
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if root is None:
            return False
        
        # if the current node is a leaf and its value is equal to the sum, we've found a path
        if root.left is None and root.right is None and root.val == sum:
            return True
        
        # recursively call to traverse the left and right sub-tree
        # return true if any of the two recursive call return true
        return self.hasPathSum( root.left, sum - root.val) \
                or self.hasPathSum(root.right, sum - root.val)

    
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
