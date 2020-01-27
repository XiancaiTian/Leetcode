# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if p and q:
                if not p.val == q.val: 
                    return False
                stack.append((p.right, q.right)) 
                stack.append((p.left, q.left)) 
            elif p and not q:
                return False
            elif not p and q:
                return False
        return True        
