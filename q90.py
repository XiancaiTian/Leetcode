class Solution:
    # 套用花花模板
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # d 代表深度，k 代表取幾個數(固定), s 代表從第幾個數字開始取
        def dfs(nums, d, k, s, curr, ans):
            if d == k:
                ans.append(curr[:])
                return
            for i in range(s, len(nums)):
                """
                Line 20: 同一個深度如果已經有一樣的數字了，就不要多算一次
                不重複的情境下 nums = [1,2,3], pick 2 becomes [[1,2], [1,3], [2,3]]
                重複的情境下 nums = [1,2,2], pick 2 becomes [[1,2], [1,2], [2,2]]
                這時候要刪掉這個2的出現,才會是正確解答                   ↑ (要避免的2)
                在同一個深度的搜尋中，他已經出現過了              ↑(前面有的2)
                才會得到正確解答: [[1,2], [2,2]]
                """
                if i > s and nums[i] == nums[i-1]:
                    # avoid repetition
                    continue
                curr.append(nums[i])
                dfs(nums, d+1, k, i+1, curr, ans)
                curr.pop()
                
        ans = []
        nums.sort()
        for k in range(0, len(nums)+1):
            dfs(nums, 0, k, 0, [], ans)
        return ans





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
