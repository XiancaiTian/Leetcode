# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """    
        maxi = root.val
        self.max = None # the true answer
        summ = self.readtree(root)
        return self.max
    
    def readtree(self, root):
        if not root:
            return 0
        # eveything got val, plus one
        # add downstream depth
        summ_left = self.readtree(root.left)
        summ_right = self.readtree(root.right)
        
        # this question is ask about path, not sum of triangle
        if root.val:
            summ_left = max(0, summ_left)
            summ_right = max(0, summ_right)
        temp = root.val + summ_left + summ_right
        self.max = max(temp, self.max)
        summ = root.val + max(summ_left, summ_right)
        return summ

'''''solution2'''''
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        '''
        trick 1: not always pick left or right
        sometimes need to have left and right
        
        trick 2: input may be negative value
        
        should refer to 
        https://github.com/XiancaiTian/Leetcode/blob/master/q124.py
        That solution looks better
        Basic idea: if left>0, bring it. if right>0 bring it.
        
        """ 
        # if only one node
        if not root.left and not root.right:
            return root.val
        
        # pick parent only
        pathsum = [root.val]
        l = self.recursion(root.left, pathsum)
        r = self.recursion(root.right, pathsum)
        
        # pick first root and a single children
        pathsum.append(root.val + max(l,r))
        # pick first root and both children
        pathsum.append(root.val + l + r )
        # pick a single children
        if root.left:
            pathsum.append(l)
        if root.right:
            pathsum.append(r)
            
        return max(pathsum)
    
        
    def recursion(self, root, pathsum):
        if not root: 
            return 0
        else:
            l = self.recursion(root.left, pathsum)
            r = self.recursion(root.right, pathsum)
            print(root.val, l, r)
            # pick parent and left or right children
            value = root.val + max(l,r)
            # or parenet only
            value = max(root.val, value)
            pathsum.append(value)
            
            # pick parent and both chidren
            pathsum.append(l + r + root.val)
            
            # pick parent only
            pathsum.append(root.val)
            
            return value
