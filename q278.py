class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 經典的左閉右開花花模板
        # 做基本的binary search
        l, r = 0, n
        while l < r:
            mid = l + (r - l)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid+1
        return l
