class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        while (num**2 <= x):
            num+=1
        return num-1
            
