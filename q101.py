class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True        
        left = []
        self.readtree_left(root.left, left)
        right = []
        self.readtree_right(root.right, right)
        return self.compare(left,right)
        
    def readtree_left(self, root, left):
        if not root:
            left.append('')
            return
        left.append(root.val)
        self.readtree_left(root.left, left)
        self.readtree_left(root.right, left)
        
    def readtree_right(self, root, right):
        if not root:
            right.append('')
            return
        right.append(root.val)
        self.readtree_right(root.right, right)
        self.readtree_right(root.left, right)
        
    def compare(self, left, right):
        print(left)
        print(right)
        for i, v in enumerate(left):
            if v!=right[i]:
                return False
        return True
