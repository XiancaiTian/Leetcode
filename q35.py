class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        for v in nums:
            if v == target:
                return i
            elif v > target:
                return i
            i += 1
        return i
