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
            if nums[mid] > nums[mid+1]:
                return mid+1
            else:
                if nums[mid] < nums[left]:
                    right = mid -1
                else:
                    left = mid + 1
        
        
