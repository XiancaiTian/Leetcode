class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
       
        row, col = len(matrix), len(matrix[0])
        is_col = False
        # add marker
        for i in range(row):
            # additional variable to save if first col need to change
            if matrix[i][0] == 0:
                is_col = True
                
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        # Iterate over the array once again 
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0 :
                    matrix[i][j] = 0
                    
        # See if the first row needs change          
        if matrix[0][0] == 0:
            for j in range(col):
                matrix[0][j] = 0
                
        # See if the first col needs change 
        if is_col:
            for i in range(row):
                matrix[i][0] = 0
                
