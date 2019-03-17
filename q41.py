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
                
