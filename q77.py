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
    
