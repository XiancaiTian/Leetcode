class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        best = (0, 0) # start, length of palindrome
        j = 1 # last
        while start+j <= len(s):
            # suspect palindrome
            suspect = s[start:start+j]
            if self.boolPalindrome(suspect) and j>=best[1]:
                best = (start, j)
                if j ==len(s):
                    break
            if start+j == len(s):
                start+=1
                j = best[1]
            else:
                j=j+1
        bstart, bj = best
        return s[bstart:bstart+bj]
    
    def boolPalindrome(self, suspect):
        mid, r = divmod(len(suspect),2)
        if mid == 0: return True
        else: return suspect[:mid]==suspect[::-1][:mid]