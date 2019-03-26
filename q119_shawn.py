class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        for i in range(rowIndex+1):
            current_line = list()
            for j in range(i+1):
                if j in (0,i):
                    current_line.append(1)
                else:
                    current_line.append(prev_line[j-1]+prev_line[j])
            prev_line = current_line
        return current_line
                    
