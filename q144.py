class Solution(object):
    def preorderTraversal(self, root):
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret
    
# my solution
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        self.preorder(root, l)
        return l
    def preorder(self, root, l):
        if root:
            l.append(root.val)
            self.preorder(root.left, l)
            self.preorder(root.right, l)
        else:
            return 
