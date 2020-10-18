class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # for loop two times
        # in first loop: swap the numbers in each iteration
        # in the second loop, detect the misplaced number
        i = 0
        while i < len(nums):
            while nums[i]-1 >= 0 and nums[i]-1 < len(nums) and nums[i]!= nums[nums[i]-1] and nums[i]!=(i+1):
                a = nums[i]
                loc = nums[i]-1
                nums[i] = nums[loc]
                nums[loc] = a
                
            i += 1
                                  
        i = 0
        ans = []
        while i < len(nums):
            if nums[i] != (i+1):
                ans.append(i+1)
            i += 1
            
        return ans
