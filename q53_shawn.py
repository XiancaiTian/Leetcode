# Kadane's Algorithm
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max = current_max = nums[0]
        for i in range(1,len(nums)):
            current_max = max(current_max+nums[i], nums[i])
            if current_max > global_max:
                global_max = current_max
        return global_max
