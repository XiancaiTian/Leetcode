class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        n = len(matrix[0])
        left, right = 0, len(matrix)*n - 1
        while left <= right:
            mid = left + (right - left)//2
            if target > matrix[mid//n][mid%n]:
                left = mid +1
            elif target < matrix[mid//n][mid%n]:
                right = mid - 1
            else:
                return True
        return False
