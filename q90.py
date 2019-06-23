class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # modify from leetcode q78
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                hold = sorted(res[i] + [n])
                if hold not in res:
                    res.append(hold)
        return res
         
