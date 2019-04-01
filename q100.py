class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        ans = True
        ans = self.dfg(p, q, ans)
        return ans
        
    def dfg(self, p, q, ans):
        if not ans:
            return ans 
        # both empty
        elif not p and not q:
            return ans
        # one of them is empty
        elif not p or not q:
            return False
        # none is empty
        elif p.val != q.val:
            return False
        ans = self.dfg(p.left, q.left, ans)
        ans = self.dfg(p.right, q.right, ans)
        return ans
