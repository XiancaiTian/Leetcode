class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        elif not ' ' in s:
            return len(s)
        else:
            s = s.strip()
            return len(s.split(' ')[-1])
