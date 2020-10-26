# Very basic solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0 
        right = len(nums)
        
        while left < right:
            mid = left + (right - left)//2
            if nums[mid]== target:
                return mid
            
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
                
        return -1

# What if the sorting is descending
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0 
        right = len(nums)
        nums.sort(reverse= True) # 故意descending看看
        
        while left < right:
            mid = left + (right - left)//2
            if nums[mid]== target:
                return len(nums) - 1 - mid
            
            if nums[mid] < target: # 關鍵 大於變小於
                right = mid
            else:
                left = mid + 1
                
        return -1
