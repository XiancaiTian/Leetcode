class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twosum(nums, target, ans):
            # Edge case: [-4,-3, -3, 1, 3, 4]
            left = 0
            right = len(nums)-1
            while left < right:
                sum_of_two = nums[left] + nums[right]
                if sum_of_two == target:
                    ans.append([nums[left], nums[right], -target])
                    left +=1
                    right -=1
                    # Note: skip if contain duplicates
                    while left < right and nums[left]==nums[left-1]:
                        left +=1
                    
                elif sum_of_two > target:
                    right -=1
                else:
                    left +=1
                            
        i = 0
        ans = []
        nums.sort()
        for i, n in enumerate(nums):
            # Note: skip if contain duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue
            else:
                twosum(nums[i+1:], - nums[i], ans)
        return ans
