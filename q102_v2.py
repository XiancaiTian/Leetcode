# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        lst = []
        if root:
            root.level = 0
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                if len(lst) <= root.level:
                    lst.append([root.val])
                else:
                    lst[root.level].extend([root.val])
                    
                if root.right:
                    root.right.level = root.level +1
                    stack.append(root.right)
                if root.left:
                    root.left.level = root.level +1
                    stack.append(root.left)

        return lst
                
