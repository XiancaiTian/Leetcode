class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = {}
        count = 0
        self.helper(root, stack, count)
        return stack.values()
    
    # recursive soln
    def helper(self, root, stack, count):
        count += 1
        if root:
            if root.left:
                self.helper(root.left, stack, count)
                
            # old version: stack.append(root.val)
            # used in q94
            
            # new version: dict soln
            if not count in stack.keys():
                stack[count] = [root.val]
            else:
                stack[count].append(root.val)
            if root.right:
                self.helper(root.right, stack, count)
        return stack
