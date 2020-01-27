# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        root.path = []
        stack = [root]
        lst = []
        while stack:
            root = stack.pop()
            if root:
                path = root.path + [str(root.val)]
                if root.right:
                    root.right.path = copy.deepcopy(path)
                if root.left:
                    root.left.path = copy.deepcopy(path)
                stack.append(root.right)
                stack.append(root.left)
            
                if not root.left and not root.right:
                    root.path += [str(root.val)]
                    lst.append("->".join(root.path))
        return lst
        
