class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        i = 0
        j = len(s) - 1
        valid_chars = '0123456789abcdefghijklmnopqrstuvwxyz'
        while j>i:
            if s[i] not in valid_chars:
                i += 1
            if s[j] not in valid_chars:
                j -= 1
            if s[i] in valid_chars and s[j] in valid_chars:
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
        return True
