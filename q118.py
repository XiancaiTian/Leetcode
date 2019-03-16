class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        first = [[1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return first
        else:
            for n in range(numRows-1):
                f = first[n]
                first.append(self.add(f))
            return first
    def add(self, first):
        prev = 0
        new = []
        for i in first:
            new.append(prev+i)
            prev = i
        return new+[1]
