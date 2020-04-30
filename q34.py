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
            print(l)
            return l if l < len(nums) and nums[l]==target else -1
        
        def upperBound(l, r):
            while l < r:
                mid = l + (r-l)//2
                if nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return l-1 if l-1 < len(nums) and nums[l-1]==target else -1

        return [lowerBound(l, r),upperBound(l, r)]
