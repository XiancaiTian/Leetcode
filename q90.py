class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """  
        '''
        # leetcode q78
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                hold = (res[i] + [n])
                res.append(hold)
        return res
        '''
        
        # leetcode q90
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                hold = sorted(res[i] + [n])
                if hold not in res:
                    res.append(hold)
        return res
