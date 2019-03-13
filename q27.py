class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new = 0
        for i in range(0, len(nums)):
            if not nums[i] == val:
                nums[new] = nums[i]
                new+=1
        return new
