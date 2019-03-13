class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        j = 1
        for i in range(1, len(nums)):
            # if same as previous, then delete it    
            if not nums[i] == nums[i-1]:
                nums[j]= nums[i]
                j+=1
        print(nums)
        return j
