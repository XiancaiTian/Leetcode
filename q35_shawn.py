class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if i == len(nums)-1:
                return i + 1
            if nums[i] < target and nums[i+1] > target:
                return i+1
