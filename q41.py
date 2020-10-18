# I don't remember why I have this solution lol...
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        i = 1
        for n in nums+nums:
            if n>0 and n == i:
                i+=1
            if i in nums:
                i+=1
        return i
                
# It's easy if you follow the solution of educative
# Edge cases are tricky: [] needs to return 1 and [1] needs to return 2

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxi_nums = len(nums)
        i = 0
        while i < maxi_nums:
            loc = nums[i] - 1
            while loc >= 0 and loc < maxi_nums and nums[i] != (i+1) and nums[i] != nums[loc]:
                a = nums[loc]
                nums[loc] = nums[i]
                nums[i] = a
                loc = nums[i] - 1
            i += 1
        
        i = 0
        while i < maxi_nums:
            if nums[i]!= (i+1):
                return (i+1)
            i += 1
            
        return maxi_nums + 1 
