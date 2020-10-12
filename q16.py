import numpy as np
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:   
        i = 0
        ans = []
        nums.sort()
        abs_diff = np.inf
        while i < len(nums)-2:
            # Note: skip if contain duplicates
            if i>0 and nums[i] == nums[i-1]:
                i += 1
            else:
                left = i+1
                right = len(nums)-1
                while left < right:
                    diff = target - (nums[i] + nums[left] + nums[right])
                    if diff == 0:
                        return target
                    if abs(diff) < abs_diff:
                        abs_diff = abs(diff)
                        ans = target - diff
                    elif diff < 0:
                        right -=1
                    else:
                        left +=1
                i += 1
        return ans
