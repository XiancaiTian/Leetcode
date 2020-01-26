# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    '''iterative'''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        stack = [root]
        while stack:
            root = stack.pop()
            if type(root) == int:
                lst.append(root)
            elif root:
                stack.append(root.right)
                stack.append(root.val)
                stack.append(root.left)                      
        return lst
            
    
    ''' recursion
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        # left middle right
        self.inorder(root, lst)
        return lst
    def inorder(self, root, lst):
        if root:
            self.inorder(root.left, lst)
            lst.append(root.val)
            self.inorder(root.right, lst)
        return
    '''
            
        
