# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        trick 1: it is possible to continuously skip two houses
        trick 2: no need to consider negative case
        """
        
        self.max = 0 # global max
        self.recursion(root)
        return self.max
    
    def recursion(self, root):
        if not root:
            return 0, 0
        else:
            left_minus2, left_minus1 = self.recursion(root.left)
            right_minus2, right_minus1 = self.recursion(root.right)
            # current node and minus2
            group_minus2 = root.val + left_minus2 + right_minus2
            # derive minus1
            group_minus1 = max(left_minus1, left_minus2) + max(right_minus1, right_minus2)
            
            self.max = max([group_minus1, group_minus2, self.max])
        return group_minus1, group_minus2

    
