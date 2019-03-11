class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        i = 1
        while i < length:
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])
                length -= 1
            else:
                i += 1
        return length
