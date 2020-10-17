class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # for loop two times
        # in first loop: swap the numbers in each iteration
        # in the second loop, detect the misplaced number
        i = 0
        while i < len(nums):
            loc = nums[i] -1
            while nums[i] != (i+1) and loc < len(nums) and loc >= 0:
                # swap
                nums[loc], nums[i] = nums[i], nums[nums[i] -1]
                loc = nums[i] -1
                
            i+=1
            
        i = 0
        while i < len(nums):
            if nums[i] != (i+1):
                return i+1      
            i += 1
            
        return 0
        
