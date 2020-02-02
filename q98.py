# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    trick 1: need to be careful about the null node
    trick 2: should reject > and <; as well as >= and <=
    trick 3: be careful [3,1,5,0,2,4,6,null,null,null,3]
    '''
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        isBST, _max, _min = self.recursion(root)
        return isBST
        
    def recursion(self, root):
        if root:
            # 
            values = [root.val]
            
            # should not assume the null node to be zero
            # further check whether is null node or not
            if root.left:
                left_isBST, left_max, left_min = self.recursion(root.left)
                if not left_isBST:
                    return False, 0, 0
                elif left_max >= root.val:
                    return False, 0, 0
                values.append(left_max)
                values.append(left_min)

            if root.right:
                rigth_isBST, right_max, right_min = self.recursion(root.right)
                if not rigth_isBST:
                    return False, 0, 0
                elif root.val >= right_min:
                    return False, 0, 0
                values.append(right_max)
                values.append(right_min)
                
            # return isBST and the maximum in left-side or minimum in right-side
            return True, max(values), min(values)
        
        return True, 0, 0
