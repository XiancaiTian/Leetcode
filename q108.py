# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #reference
    #https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/35224/Python-optimal-solution
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        self.nums = nums
        return self.recursion(0, len(nums)-1)
        
    def recursion(self, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(self.nums[mid])
        root.left = self.recursion(start, mid-1)
        root.right = self.recursion(mid+1, end)
        return root
