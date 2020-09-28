class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_sum = dict()
        max_length = 0
        window_start = 0
        
        for window_end in range(0, len(s)):            
            if s[window_end] in window_sum:
                window_start = max(window_start, window_sum[s[window_end]]+1)
            window_sum.update({s[window_end]: window_end})
            max_length = max(max_length,  window_end - window_start +1 )
            
        return max_length
