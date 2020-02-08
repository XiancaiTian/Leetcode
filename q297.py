# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
        # serialize to [1,2,3,null,null,4,5] is  more difficult
        # should serialize to ['1', '2', 'n', 'n', '3', '4', 'n', 'n', '5', 'n', 'n']
        # https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74259/Recursive-preorder-Python-and-C%2B%2B-O(n)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        lst = []
        self.read(root, lst)
        return  ' '.join(lst)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(' ')
        def write():
            if lst:
                val = lst.pop(0)
                if val =='n':
                    return
                root = TreeNode(val)
                root.left = write()
                root.right = write()
                return root
            
        return write()
        
    def read(self, root, lst):
        if root:
            lst.append(str(root.val))
            self.read(root.left, lst)
            self.read(root.right, lst)
        else:
            lst.append('n')

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
