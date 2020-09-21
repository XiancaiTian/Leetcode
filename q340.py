# using educative template

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window_sum = collections.defaultdict(int)
        max_length = 0
        window_start = 0

        for window_end in range(0, len(s)):
            window_sum[s[window_end]] += 1
            while len(window_sum) > k:
                window_sum[s[window_start]] -= 1
                if window_sum[s[window_start]] == 0:
                     window_sum.pop(s[window_start])
                window_start += 1                
            max_length = max(max_length,  window_end - window_start +1 )
            
        if max_length == 0:
            return 0
        return max_length
