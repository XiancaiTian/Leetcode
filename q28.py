class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        elif not needle in haystack:
            return -1
        elif needle == haystack:
            return 0
        else:
            leng = len(needle)
            for i in range(len(haystack)-leng+1):
                if needle == haystack[i: i+leng]:
                    return i
