class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_sum, best_sum = 0, nums[0]
        for v in nums:
            prev_sum += v
            best_sum = max(prev_sum, best_sum)
            if prev_sum <0:
                prev_sum = 0
        return best_sum
