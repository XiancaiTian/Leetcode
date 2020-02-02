# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    trick 1: use dfs and reverse the list
    '''
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lst = []
        self.recursion(root, 0, lst)
        return lst[::-1]
    
    def recursion(self, root, level, lst):
        if root:
            if len(lst)<level+1:
                lst.append([root.val])
            else:
                lst[level].append(root.val)
            self.recursion(root.left, level+1, lst)
            self.recursion(root.right, level+1, lst)
