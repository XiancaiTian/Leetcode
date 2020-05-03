class Solution:
    def mySqrt(self, x: int) -> int:
        # Edge cases...
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        # mid的平方會大於input x 嗎?
        def higerThan(mid, x):
            return mid**2 > x
        
        # 套用lower bound binary search template
        # 找到第一個平方大於input的數
        # 如果input = 8, 1*1 -->F, 2*2 -->F, 3*3 -->T, 則binary search會return 3
        # 因為題目要求只想看integer部分，所以最後答案應該是3-1=2
        l, r = 0, x
        while l < r:
            mid = l + (r-l)//2
            if higerThan(mid,x):
                r = mid
            else:
                l = mid + 1
        return l-1


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
            
