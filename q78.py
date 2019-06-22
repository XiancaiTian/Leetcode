class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res += [res[i] + [n]]
        return res
    
    
class Solution(object):
    def subsets(self, nums):
        self.nums = nums
        ans = []
        length = len(nums)
        for num in range(length+1):
            ans += self.pick(length, abs(num))
        return ans
    
    def pick(self, n , k):
        if k == 0:
            return [[]]
        else:
            return [ele + [self.nums[val-1]] for val in range(k,n+1) for ele in self.pick(val-1, k-1)]
