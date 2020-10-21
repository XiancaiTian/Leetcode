class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if root is None:
            return False
        
        # if the current node is a leaf and its value is equal to the sum, we've found a path
        if root.left is None and root.right is None and root.val == sum:
            return True
        
        # recursively call to traverse the left and right sub-tree
        # return true if any of the two recursive call return true
        return self.hasPathSum( root.left, sum - root.val) \
                or self.hasPathSum(root.right, sum - root.val)
