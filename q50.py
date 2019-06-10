class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0 and n < 0 :
            return float("inf")
        elif n == 0:
            return 1
        elif n < 0:
            return 1/ self.Pow(x, abs(n))
        else:
            return self.Pow(x, abs(n))
            
    def Pow(self, x, n):
        if n == 1:
            return x
        q, r = divmod(n, 2)
        val = self.Pow(x, q)
        val = val*val
        if r:
            val = val*x
        return val
