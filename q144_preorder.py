# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''iterative
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                lst.append(node.val)
                stack.append(node.right)   
                stack.append(node.left)
        return lst
    
    '''
    '''recursive'''
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        self.preorder(root, lst)
        return lst
    def preorder(self, root, lst):
        if root:
            lst.append(root.val)
            self.preorder(root.left, lst)
            self.preorder(root.right, lst)
        return
