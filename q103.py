# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    trick 1: modify q107
    '''
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lst = []
        self.recursion(root, 0, lst)
        return lst
    
    def recursion(self, root, level, lst):
        if root:
            # first value in list; any position is fine
            if len(lst)<level+1:
                lst.append([root.val])
                
            # odd level, left to right order
            elif level%2:
                lst[level].append(root.val)
                
            # even level, right to left order
            else:
                lst[level].insert(0, root.val)
            
            level += 1
            self.recursion(root.right, level, lst)
            self.recursion(root.left, level, lst)
            
