class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def generator(r1, r2, c1, c2):
            r, c = r1, c1
            for c in range(c1, c2, 1):
                yield r, c
            for r in range(r1+1, r2, 1):
                yield r, c
            for c in range(c2-2, c1-1, -1):
                yield r, c
            for r in range(r2-2, r1, -1):
                yield r, c
                
        r1, r2 = 0, n
        value = 1
        matrix = [[0 for i in range(n)] for i in range(n)]
        while r1<r2:
            for a, b in generator(r1,r2,r1,r2):
                matrix[a][b] = value
                value+=1
            r1+=1
            r2-=1
        return matrix
