class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def canThreshold(nums, mid, threshold):
            total = 0
            for n in nums:
                total += (n-1)//mid +1
                if total > threshold:
                    return False
            return True
        
        # binary search
        l, r = 1, max(nums)
        while l < r:
            mid = l + (r-l)//2
            if canThreshold(nums, mid, threshold):
                r = mid
            else:
                l = mid + 1
        return l
