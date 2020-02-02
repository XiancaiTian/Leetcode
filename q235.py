# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    trick 1: note the format of ans, p, q; it is not asking for integer but node
    trick 2: be careful about overwrite

    '''
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.p = p.val
        self.q = q.val
        found_p, found_q = self.recursion(root)
        return self.ans
        
    def recursion(self, root):
        # try to skip after finding a solution
        if not root or not self.lack_ans():
            return False, False
        print(root.val, root.val == self.q)
        found_p1, found_q1 = self.recursion(root.left)
        found_p2, found_q2 = self.recursion(root.right)
        found_p = True if found_p1 or found_p2 or self.p == root.val else False
        found_q = True if found_q1 or found_q2 or self.q == root.val else False
        
        # only want the first answer
        if found_p and found_q and self.lack_ans():
            self.ans = root
        return found_p, found_q
    
    def lack_ans(self):
        try:
            self.ans
            return False
        except AttributeError:
            return True
        
'''standard solution'''
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:    
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:    
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root
