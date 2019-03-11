# Runtime: 5244 ms, faster than 16.44% of Python3 online submissions for Two Sum.
# Memory Usage: 13.8 MB, less than 25.44% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
