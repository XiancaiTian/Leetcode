# LEETCODE Q238

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        
        left, right = 1, n
        while left <= right:
            mid = (left+right) // 2
            print(left, right, mid)
            if not isBadVersion(mid) and isBadVersion(mid+1):
                return mid+1
            elif isBadVersion(mid):
                right = mid
            else:
                left = mid
                
# LEETCODE Q35      
class Solution(object):
def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums)-1

    while left<=right:
        mid = (left + right)//2 
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid -1

    return left

                
 
                
                
