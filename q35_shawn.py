class Solution:
    # 55.4%
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

class Solution:
    def searchInsert(self, nums, target):
        for idx, v in enumerate(nums):
            if v == target:
                return idx
            elif target < v:
                return idx
        return idx+1
