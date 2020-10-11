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

# alternative two pointer solution
class Solution:
def removeDuplicates(self, nums: List[int]) -> int:
    fast = 0
    slow = 0
    while fast < len(nums) -1: 
        if nums[fast]!= nums[fast+1]:
            slow += 1
            nums[slow] = nums[fast+1]
        fast +=1
    #print(nums[:slow+1])
    return slow +1
