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
        
        return self.recursion(n+1,k)

    def recursion(self, n, k):
        '''
        n: ranges from 1,2,n
        k: num of selection
        '''
        ans = []
        for i in range(1, n):
            if k-1>0:
                sub = [lst + [i] for lst in self.recursion(i, k-1)]
            else:
                sub = [[i]]
            ans.extend(sub)
        return ans
