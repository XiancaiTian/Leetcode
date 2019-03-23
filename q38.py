class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        if n == 1:
            return s
        else:    
            for i in range(1, n):
                s = self.countt(s)
            return s
    def countt(self, s):
        prev, previd = s[0], 0
        new =''
        for idx in range(1, len(s)):
            if prev != s[idx]:
                new += str(len(s[previd:idx]))+str(prev)
                prev, previd = s[idx], idx
        new += str(len(s[previd:]))+str(prev)
        return new
