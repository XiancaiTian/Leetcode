class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [[j,i] for j, jv in enumerate(nums) for i, iv in enumerate(nums) if iv+jv == target and i!=j][0]
