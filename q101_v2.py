# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:    
        if root:
            return self.compare(root.left, root.right)
        return True
    
    def compare(self, p: TreeNode, q: TreeNode) -> bool:
        '''modify from q100_v2.py'''
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if p and q:
                if not p.val == q.val: 
                    return False
                stack.append((p.right, q.left)) 
                stack.append((p.left, q.right)) 
            elif p and not q:
                return False
            elif not p and q:
                return False
        return True
