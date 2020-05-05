class Solution:
    # 套用花花模板
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # dfs function 跟Leetcode 77 完全一樣
        # d 代表深度，k 代表取幾個數(固定), s 代表從第幾個數字開始取
        # nums 代表可以選的數字範圍
        def dfs(nums, d, k, s, curr, ans):
            if d == k:
                ans.append(curr[:])
                return
            for i in range(s, len(nums)):
                curr.append(nums[i])
                dfs(nums, d+1, k, i+1, curr, ans)
                curr.pop()
                
        ans = []
        for k in range(0, len(nums)+1):
            dfs(nums, 0, k, 0, [], ans)
        return ans


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

 # the most easy solution
 class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for val in nums:
            for subset in ans:
                if val not in subset:
                    ans.append(subset+[val])
        return ans
