class Solution:
    # 取K個數，nums = [1,2,3,4,..,n], 找combination
    def combine(self, n: int, k: int) -> List[List[int]]:
        # d 代表深度，k 代表取幾個數(固定), s 代表從第幾個數字開始取
        # nums 代表可以選的數字範圍
        def dfs(nums, d, k, s, curr, ans):
            if d == k:
                ans.append(curr[:])
                return
            for i in range(s, n):
                curr.append(nums[i])
                dfs(nums, d+1, k, i+1, curr, ans)
                curr.pop()
                
        # 這個步驟有點浪費memory, 但是增加可讀性
        nums = [i + 1 for i in range(n)]
        ans = []
        dfs(nums, 0, k, 0, [], ans)
        return ans


class Solution(object):
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        else:
            return [ele + [val] for val in range(k,n+1) for ele in self.combine(val-1, k-1)]
    
# Helena's solution, based on recursion    
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # recursion soln
        # https://www.youtube.com/watch?v=qzdTZWW1X8A
        ans = []
        for i in range(1, n+1):
            if k-1 > 0:
                sub = [[i] + lst for lst in self.combine(i-1, k-1)]
            elif k == 1:
                sub = [[i]]
            else:
                sub = []
            ans.extend(sub)
        return ans
'''
combine(5,3)
[1+ combine(0, 2)]  --> None
[2,+ combine(1, 2)] --> None
[3,+ combine(2, 2)] -->[3, 2, 2], [3, 2, 1]
[4,+ combine(3, 2)] -->[4, 1, 2], [4, 1, 3],.....
[5,+ combine(4, 2)] --> ......
'''
