# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    concept: recursive every node while saving the height
    '''
    def isBalanced(self, root):
        ans = self.height(root, 0)
        return False if ans < 0 else True 
        
    def height(self, root, cum_height):
        if cum_height == -1:
            return -1
        elif root:
            cum_height +=1
            l = self.height(root.left, cum_height)
            r = self.height(root.right, cum_height)
            
            if abs(l-r) <= 1:
                return max(l,r)
            else:
                return -1
        else:
            return cum_height
