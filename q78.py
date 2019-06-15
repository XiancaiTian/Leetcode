class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res += [res[i] + [n]]
        return res
