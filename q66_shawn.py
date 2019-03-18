class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = 0
        for d in digits:
            s = 10*s + d
        s += 1
        res = list()
        while s > 0:
            r = s%10
            s = s//10
            res.insert(0,r)
        return res
