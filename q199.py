# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        self.readtree(root, 0)
        return self.ans
    
    def readtree(self, root, loc):
        if not root:
            return
        if loc <= len(self.ans)-1:
            self.ans[loc] = root.val
        else:
            self.ans.insert(loc,root.val)
        self.readtree(root.left, loc+1)
        self.readtree(root.right, loc+1)
        
        
''' solution 2'''

class Solution(object):
    '''
    trick 1: modify q107, q103
    '''
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        self.recursion(root, 0, lst)
        return lst
    
    def recursion(self, root, level, lst):
        if root:
            # only care about first value in each level
            if len(lst)<level+1:
                lst.append(root.val)

            level += 1
            self.recursion(root.right, level, lst)
            self.recursion(root.left, level, lst)
           
