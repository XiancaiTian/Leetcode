# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''iterative'''
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        stack = [root]
        while stack:
            root = stack.pop()
            if type(root) == int:
                lst.append(root)
            elif root:
                stack.append(root.val)
                stack.append(root.right)
                stack.append(root.left)  
        return lst
        
    '''recursive
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        self.postorder(root, lst)
        return lst
        
    def postorder(self, root, lst):
        if root:
            self.postorder(root.left, lst)
            self.postorder(root.right, lst)
            lst.append(root.val)
        return
    '''
