class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        pivot = self.find_pivot(nums, target)
        if target <= nums[-1]:
            index = self.find_value(nums[pivot:], target, pivot)
        else:
            index = self.find_value(nums[:pivot], target, 0)
        return index
        
    def find_value(self, nums, target, pivot):
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left + right) //2
            if nums[mid] == target:
                return pivot + mid
            else:
                if target > nums[mid] :
                    left = left + 1
                else:
                    right = right -1
        return -1
        
    
    def find_pivot(self, nums, target):
        left, right = 0, len(nums)-1
        while left<right:
            mid = (left + right) //2
            if nums[mid] > nums[mid+1]:
                return mid+1
            else:
                if nums[left] < nums[mid]:
                    left = left + 1
                if nums[right] > nums[mid]:
                    right = right -1
        return 0

        
