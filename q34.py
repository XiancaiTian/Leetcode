# More intuitive solution

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer_lst = [-1, -1]
        
        # speed up a little bit
        if not nums:
            return answer_lst

        # find lower bound
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left + (right - left)//2
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if left < len(nums) and left >= 0 and nums[left]==target:   
            answer_lst[0] = left

        # find upper bound
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left + (right - left)//2
            
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        if (left-1) < len(nums) and (left-1) >= 0 and nums[left-1]==target: 
            answer_lst[1] = left-1
            
        
        return answer_lst






class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        if r == 0: return [-1,-1]
        if r == 1:
            return [0,0] if nums[0] == target else [-1, -1]
        
        def lowerBound(l, r):
            while l < r:
                mid = l + (r-l)//2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l if l < len(nums) and nums[l]==target else -1
        
        def upperBound(l, r):
            while l < r:
                mid = l + (r-l)//2
                if nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return l-1 if l-1 < len(nums) and nums[l-1]==target else -1

        return [lowerBound(l,r), upperBound(l, r)]
