from collections import deque

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A)-1
        
        ans = deque()
        while left <= right:
            if abs(A[left])>= A[right]:
                ans.appendleft(A[left]**2)
                left +=1
            else:
                ans.appendleft(A[right]**2)
                right -=1
                
        return list(ans)
