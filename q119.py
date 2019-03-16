class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        row = [1]
        if rowIndex == 0:
            return row
        for n in range(rowIndex):
            row = self.add(row)
        return row
    
    def add(self, row):
        prev = 0
        new = []
        for i in row:
            new.append(prev+i)
            prev = i
        return new+[1]
