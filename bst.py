# LEETCODE Q278

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
            
            # mid = (left+right) // 2         # may cause overflow
            mid = left + (right - left) // 2  # better
            
            print(left, right, mid)
            if not isBadVersion(mid) and isBadVersion(mid+1):
                return mid+1
            elif not isBadVersion(mid-1) and isBadVersion(mid):
                return mid
            
            elif isBadVersion(mid):
                right = mid-1
            else:
                left = mid+1
                
                
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

# LEETCODE Q33               
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1 

        pivot = self.find_pivot(nums, target)
        if target <= nums[-1]:
            index = self.find_value(nums[pivot:], target, pivot)
        else:
            index = self.find_value(nums[:pivot], target, 0)
        return index


    # template: may find nothing
    def find_value(self, nums, target, base):
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left + right) //2
            if nums[mid] == target:
                return base + mid
            else:
                if target > nums[mid] :
                    left = mid + 1
                else:
                    right = mid -1
        return -1

    # template: must find something
    def find_pivot(self, nums, target):
        left, right = 0, len(nums)-1 
        if nums[left] < nums[right]:
            return 0

        while left<=right:
            mid = (left + right) //2
            print(left, right, mid)
            if nums[mid] > nums[mid+1]:
                return mid+1
            else:
                if nums[mid] < nums[left]:
                    right = mid -1
                else:
                    left = mid + 1






