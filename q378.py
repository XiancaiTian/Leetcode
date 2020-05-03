class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = matrix[0][0]
        r = matrix[-1][-1]
        n_row, n_col = len(matrix), len(matrix[0])
        
        def lessOrEqual(k):
            count = 0
            for n in range(n_row):
                row, col = matrix[n_row-n-1], 0
                while col < n_col and row[col] <= k:
                    col += 1
                count += col
            return count>= k                           
        
        while l < r:
            m = l + (r-l)//2
            if lessOrEqual(m):
                r=m
            else:
                l=m+1
        return l
    

class Solution(object):
    def kthSmallest(self, matrix, k):
        
        def count_le(num):
            """How many elements are less than or equal to `num`?"""
            count = 0
            # Note that `col` is not reset for each row: we continue
            # on because the columns are sorted as well. i.e. the
            # cell one up is guaranteed to be smaller-or-equal to
            # current cell.
            col = 0
            
            # We start at bottom left, going up and right as necessary.
            # If we started at top-left, imagine we go right because numbers
            # are less-than-equal to num, when that condition breaks and we
            # must go a row down, that number is even bigger! At that point we
            # don't know if actually the number to the left of this one is also
            # bigger (and thus should not be counted.)
            for row in reversed(matrix):
                # Go left to right until we reach an element
                # that is not less than or equal to `num`.
                while col < cols and row[col] <= num: 
                    col += 1
                # All the elemnts to the left are less than
                # `num`, so we count them.
                count += col
            return count
        
        rows = cols = len(matrix)
        lo = matrix[0][0]  # Min number in matrix
        hi = matrix[rows - 1][cols - 1]  # Max number in matrix
        
        while lo < hi:
            guess = (lo + hi) // 2
            x = count_le(guess)
            if x < k:
                lo = guess + 1
            else:
                # Not guess-1, because this `guess` might be == k, 
                # and end up being the correct answer.
                hi = guess
        return lo
