class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        window_start, max_length = 0, 0
        zero_frequency = 0
        
        for window_end, right_char in enumerate(A):
            if right_char == 0:
                zero_frequency += 1
                
            while zero_frequency > K:
                if A[window_start] == 0:                    
                    zero_frequency -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)
            
        return max_length
