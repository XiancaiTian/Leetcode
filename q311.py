class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: 
            return None
        m, n, l = len(A), len(A[0]), len(B[0])
        C = [[0 for _ in range(l)] for _ in range(m)]
        
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                for j, eleB in enumerate(B[k]):
                    C[i][j] += eleA * eleB
        return C
