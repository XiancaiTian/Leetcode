class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n ==1:
            return 'a'
        elif n == 2:
            return 'ab'
        # n>=3
        else:
            if n%2 == 0:
                return 'a'* (n-1) +'b'
            else:
                return 'a'*(n)
