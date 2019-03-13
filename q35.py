class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        for v in nums:
            if v == target:
                return i
            elif v > target:
                return i
            i += 1
        return i

    
## solution 2: faster than 100.00% , less than 69.35% 
class Solution(object):
def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    i = 0
    for i, v in enumerate(nums):
        if v == target:
            return i
        elif v > target:
            return i
    return i+1
