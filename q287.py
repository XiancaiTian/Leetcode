# cyclic sort solution suggested by educative
# Find the Duplicate Number (easy)

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        maxi_len = len(nums)
        while i < maxi_len:
            loc = nums[i] -1
            while loc >=0 and loc < maxi_len and nums[i] != nums[loc] and nums[i]!= (i+1):
                a = nums[loc]
                nums[loc] = nums[i]
                nums[i] = a
                loc = nums[i] -1
            i += 1
        
        i = 0
        while i < maxi_len:
            if nums[i] != (i+1):
                return nums[i]
            i +=1
        return 0
